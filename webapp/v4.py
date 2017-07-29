import requests
import json


def main(owner=None , repoName=None ):

    if owner is None:
          owner="csehamid"
    else:
          owner = owner


    if repoName is None:
        repoName="crossroad"
    else:
        repoName = repoName

    outputArray=[]


    query =('{repository(name: "' + repoName +'", owner: "'+owner+'") { ref(qualifiedName: "master") { target { ... on Commit { id history(first: 100) { pageInfo { hasNextPage } edges { node { message}}}}}}}}')
	
	
	#add your Github Token here
    headers = {'Authorization': 'token XXX'}

    r1=requests.post('https://api.github.com/graphql', json.dumps({"query": query}), headers=headers)


    result= r1.json()

    i=0
    while (i<len(result[u'data'] [u'repository'] [u'ref'][u'target'][u'history'][u'edges'])):
        line = result[u'data'] [u'repository'] [u'ref'][u'target'][u'history'][u'edges'][i][u'node'][u'message']
        outputArray.append(line)
        i=i+1
    return outputArray

if __name__ == "__main__":
    main()
