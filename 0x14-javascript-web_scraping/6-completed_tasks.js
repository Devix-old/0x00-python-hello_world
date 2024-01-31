#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error.message);
  } else if (response.statusCode === 200) {
    const todosData = JSON.parse(body);

    // Create an object to store the count of completed tasks for each user id
    const completedTasksByUser = {};

    // Iterate through the todos and count completed tasks by user id
    todosData.forEach(todo => {
      if (todo.completed) {
        if (completedTasksByUser[todo.userId]) {
          completedTasksByUser[todo.userId]++;
        } else {
          completedTasksByUser[todo.userId] = 1;
        }
      }
    });

    console.log(completedTasksByUser);
  } else {
    console.error(`Error: Unexpected status code - ${response.statusCode}`);
  }
});
