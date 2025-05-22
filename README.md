# Student Marks API

A simple Python API deployed on Vercel that returns student marks.

## Usage

Make GET requests to:
```
https://your-app.vercel.app/api?name=X&name=Y
```

Returns:
```json
{
  "marks": [mark_for_X, mark_for_Y]
}
```

## Examples

- `https://your-app.vercel.app/api?name=x&name=M` returns `{"marks": [63, 69]}`
- `https://your-app.vercel.app/api?name=pLl2z1lD` returns `{"marks": [98]}`
- `https://your-app.vercel.app/api?name=nonexistent` returns `{"marks": [null]}`

## Deployment

1. Install Vercel CLI: `npm i -g vercel`
2. Run `vercel` in the project directory
3. Follow the prompts to deploy