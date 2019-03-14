
function turnOnLed() {
  var url = 'api/led'
  var data = {name: 'Wolvs', action: 'turn on'};

  fetch(url, {
    method: 'POST',
    body: JSON.stringify(data),
    headers:{
      'Content-Type': 'application/json'
    }
  }).then(res => res.json())
    .then(response => {
      console.log('Success:', response)
      alert(`Deu bom!\nmessage: ${response.message}`)
    })
    .catch(error => {
      console.error('Error:', error)
      alert('Deu ruim')
    });
}
