

document.addEventListener('DOMContentLoaded', function() {
  setInterval(createBalls, 7000); // Create balls every 5 seconds
});

function createBalls() {
  const numBalls = 3; // Number of balls to create
  const balls = [];

  // Create balls and set initial positions
  for (let i = 0; i < numBalls; i++) {
    const ball = document.createElement('div');
    ball.classList.add('ball');
    document.body.appendChild(ball);
    balls.push(ball);

    // Set random positions for balls
    let randomX, randomY;
    do {
      randomX = Math.random() * (window.innerWidth - 20) + 10;
      randomY = Math.random() * (window.innerHeight - 20) + 10;
    } while (checkCollision(randomX, randomY, balls));

    ball.style.left = `${randomX}px`;
    ball.style.top = `${randomY}px`;
  }
}

function checkCollision(x, y, balls) {
  for (let ball of balls) {
    const ballX = parseFloat(ball.style.left);
    const ballY = parseFloat(ball.style.top);
    const distance = Math.sqrt((ballX - x) ** 2 + (ballY - y) ** 2);

    if (distance < 20) { // Minimum distance between balls (20px radius)
      return true;
    }
  }
  return false;
}



document.addEventListener('DOMContentLoaded', function() {
    var closeButton = document.getElementById('closeButton');
    var scrapButton = document.getElementById('scrapButton');
    var predictedProduct = document.getElementById('predictedProduct');
    var exstatus = document.getElementById('status');
  
    closeButton.addEventListener('click', function() {
      window.close(); 
    });

    document.getElementById("scrapButton").addEventListener("click", function() {
      document.getElementById("scrapButton").style.display="none";
      var imageElement = document.getElementById("load");
      imageElement.style.display = "block";
  });
     
    
  
    scrapButton.addEventListener('click', function() {
   
      chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, { action: 'getURL' }, function(response) {
       
          if (chrome.runtime.lastError) {
            console.error('Error in chrome.tabs.sendMessage:', chrome.runtime.lastError.message);
            alert('Failed to send test message from popup script.');
          } else if (response && response.url) {
            fetch('http://127.0.0.1:5000/receive-url', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ url: response.url }),
                    })
                    .then(response => response.json())
                    .then(data => {
                        console.log(data);
                        if (data.status === 'success') {
                          document.getElementById('status').style.color="green";
                          exstatus.textContent=`Product and Logo Verified Successfully!`;
                          predictedProduct.textContent = `${data.predicted_product}`;
                          document.getElementById("demo").textContent=`The Product is `;
                          pc.textContent = `We confirm it by : ${data.percent} %`;
                        }
                        else if (data.status === 'partial1') {
                          exstatus.textContent=`Logo Verification Failed!!`;
                          document.getElementById("demo").textContent=`It looks like ${data.predicted_product}`;
                          pc.textContent = `Fake Logo or Logo doesn't exist!`;
                        }
                        else if (data.status === 'partial2') {
                          exstatus.textContent=`Logo Verification Failed!! Product and Logo Mismatched!!`;
                          document.getElementById("demo").textContent=`It looks like ${data.predicted_product}`;
                          pc.textContent = `Logo Identified:${data.predicted_logo}`;
                        }
                        else if (data.status === 'partial3') {
                          exstatus.textContent=`Description Verification Failed!! Product and Description Mismatched!!`;
                        }
                        else if(data.status === 'failed'){
                          exstatus.textContent=`Product Verification Failed`;
                          predictedProduct.textContent = `Product Mismatch: 1st - ${data.predicted_product1}, 2nd - ${data.predicted_product2}`;
                        } 
                        else {
                          predictedProduct.textContent = 'Failed to predict product.';
                        }
                        var imageElement = document.getElementById("load");
                        imageElement.style.display = "none";
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
          } else {
            urlDisplay.textContent = 'Failed to receive URL from content script.';
          }
        });
      });
    });
  });
  