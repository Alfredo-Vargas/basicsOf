# jq a lightweight and flexible command-line jSON processor

## Pretty formatter

```console
<json-input> | jq .
```

## Get Value of a particular Key

- `.[]` : retrieves the array of json objects
- We get the values whose key has location

```console
<json-input> | jq '.[].location'
```

- We can filter the retrieve of values by piping (ex. using the **select** filter)
- Show objects whose location is "Remote"

```console
<json-input> | jq '.[] | select(.location=="Remote")'
```

## Transform Output

```console
<json-input> | jq '.[] | select(.location=="Remote") | {company:.company, url:.url, tittle:.title}'
```

- To retrieve the output as pure strings (double quoted)

```console
<json-input> | jq '.[] | select(.location=="Remote") | company,.company, url,.url, tittle,.title'
```

- To retrieve the strings as raw values

```console
<json-input> | jq -r '.[] | select(.location=="Remote") | company,.company, url,.url, tittle,.title'
```


