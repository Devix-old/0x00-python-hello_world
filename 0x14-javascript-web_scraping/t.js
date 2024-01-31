#!/usr/bin/node

const request = require("request");
url = "https://swapi-api.alx-tools.com/api/films/"

request(url, "utf-8", (error, content, body)=> {
	let i = 0;
	body = JSON.parse(body)
	for (let film of body.results)
	{
		for (let character of film.characters)
		{
			if (character.includes("18"))
			{
				i++;
			}
		}
	}
	console.log(i)
})
