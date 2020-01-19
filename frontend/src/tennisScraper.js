import axios from "axios";

export function getTennisData(callback) {
    axios
      .get('http://127.0.0.1:5000/tennisData')
      .then(function (response) {
        callback(response)
      })
}