# Fiscal-FR MCP Consumer Integration Contract

This document is the public consumer-facing contract for integrating with the `fiscal-fr` MCP server.

## Purpose

This contract defines what external clients need in order to:
- connect to the MCP server,
- discover available tools,
- call tools with valid payloads,
- handle responses and errors predictably.

## Scope

This is an external integration document only.
It intentionally excludes internal implementation details, repository internals, private operational configuration, and sensitive information.

## MCP Identity

- Server name: `fiscal-fr-mcp`
- Protocol: MCP over JSON-RPC 2.0

## Supported Transports

- `stdio`
- HTTP stateless

HTTP MCP endpoints:
- `POST /mcp` (primary)
- `GET /mcp` (for MCP client compatibility)
- `DELETE /mcp` (stateless session close)

## Authentication (Client View)

HTTP calls to `/mcp` require a valid Bearer token.

Expected header:
```http
Authorization: Bearer <token>
```

If authentication is missing or invalid:
- HTTP `401`
- `WWW-Authenticate` header is returned

## Authentication Provisioning (Operator View)

For local/operator provisioning, authentication records are stored in MongoDB.

Supported repository commands:
- `npm run seed:auth` to reseed the full auth dataset from `scripts/seeds/*.json`
- `npm run create:user` to create a single interactive user without wiping existing records

The interactive command prompts for:
- `email`
- `userId` (defaults to the email)
- `active` flag
- generated password displayed after creation

### Self-Service Token Portal

The HTTP server exposes a self-service portal for operators to obtain a long-lived Bearer token without CLI access:

- `GET /token-portal` — renders a login form (HTML)
- `POST /token-portal` — authenticates with email/password and issues a token valid for 365 days

Default response: HTML page displaying the token and a ready-to-use Claude Code MCP configuration snippet.

Programmatic (JSON) response — send `Accept: application/json`:

```http
POST /token-portal
Content-Type: application/x-www-form-urlencoded
Accept: application/json

email=user@example.com&password=secret
```

```json
{ "token": "<bearer-token>" }
```

Tokens issued by this portal are stored in MongoDB (`apiKeys` collection) and can be revoked by disabling the user or the key.

## Exposed OAuth Discovery and Flow Endpoints

- `GET /.well-known/oauth-authorization-server`
- `GET /.well-known/oauth-protected-resource`
- `GET /.well-known/oauth-protected-resource/mcp`
- `POST /oauth/register`
- `GET /oauth/authorize`
- `POST /oauth/authorize`
- `POST /oauth/token`

## JSON-RPC Contract

### Standard Tool Response Shape

Tool results are returned in:
- `result.content[0].type = "text"`
- `result.content[0].text = serialized JSON`

Clients must parse `content[0].text` as business JSON.

### Contractual Error Types

Tool errors:
- `INVALID_INPUT`
- `UNKNOWN_TOOL`
- `UNKNOWN_STEP` (for `guide_filing_step`)

Expected error shape:
- `isError: true`
- `content[0].text` contains a serialized business error JSON

Authentication errors:
- HTTP `401`
- JSON-RPC Unauthorized error payload

## Tool Catalog

Exposed tools:
- `qualify_tax_profile`
- `list_supporting_documents`
- `detect_review_points`
- `build_pre_declaration`
- `estimate_impact`
- `compare_tax_options`
- `guide_filing_step`

### 1) `qualify_tax_profile`

Goal:
- qualify the tax situation and return a structured profile.

Required input:
- `householdStatus`
- `dependentsCount`
- `incomeTypes`

Optional input:
- `charges`, `events`, `dependentContexts`, `donationContexts`, `homeServiceContexts`, `alimonyContexts`

Primary output fields:
- `factsConfirmed`, `hypotheses`, `pointsToConfirm`, `nextQuestions`
- `complexity`, `mvpDecision`
- `detectedTopics`, `suggestedCaseCodes`, `requiredDocuments`, `onlineUiHints`
- `knowledgeRecommendations`, `sourceCoverage`

### 2) `list_supporting_documents`

Goal:
- produce the supporting-document checklist.

Required input:
- `profileSnapshot`

Optional input:
- `alreadyAvailableDocuments`, `knownFacts`

Primary output fields:
- `required`, `recommended`, `missing`, `notes`, `profileSummary`

### 3) `detect_review_points`

Goal:
- detect blocking and non-blocking review points.

Required input:
- `profileSnapshot`

Optional input:
- `knownFacts`, `declaredAmounts`

Primary output fields:
- `reviewPoints`, `hasBlockingPoints`, `summary`

### 4) `build_pre_declaration`

Goal:
- build a structured pre-filing draft.

Required input:
- `profileSnapshot`

Optional input:
- `declaredAmounts`, `knownFacts`

Primary output fields:
- `sections`, `pointsToConfirm`, `draftStatus`

### 5) `estimate_impact`

Goal:
- return an indicative tax-impact estimate.

Required input:
- `profileSnapshot`

Optional input:
- `declaredAmounts`, `options`

Primary output fields:
- `summary`, `estimation`, `details`, `warnings`, `disclaimer`

### 6) `compare_tax_options`

Goal:
- compare tax arbitrage options.

Required input:
- `householdStatus`, `dependentsCount`, `incomeTypes`

Primary optional input:
- `estimatedTmi`, `includeDeferredCsgBenefit`, `incomeYear`
- `salary`, `realExpenses`, `capitalIncome`, `rentalIncome`, `adultChild`
- `requestedArbitrages`

Primary output fields:
- `comparisons`, `globalWarnings`, `disclaimer`

### 7) `guide_filing_step`

Goal:
- provide step-by-step filing guidance.

Required input:
- `currentStep`

Optional input:
- `knownContext`

Primary output fields:
- `verifyNow`, `frequentOmissions`, `traps`
- `keyCaseCodes`, `notes`, `contextualHighlights`, `availableSteps`

## Recommended Client Call Sequence

1. `tools/list`
2. `qualify_tax_profile`
3. `list_supporting_documents`
4. `detect_review_points`
5. `build_pre_declaration`
6. `estimate_impact`
7. `compare_tax_options`
8. `guide_filing_step`

## JSON-RPC Examples (HTTP)

### tools/list

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {}
}
```

### tools/call

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "qualify_tax_profile",
    "arguments": {
      "householdStatus": "single",
      "dependentsCount": 0,
      "incomeTypes": ["salary"]
    }
  }
}
```

## Compatibility Policy

Any change to contractual surface (tool list, required fields, error types, response contract) must be versioned and communicated to consumers.
