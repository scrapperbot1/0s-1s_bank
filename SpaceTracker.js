async function sendData() {
  const data = {
    name: "Laptop",
    price: 2999.99
  };

  try {
    const response = await fetch("http://127.0.0.1:8000/items/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"  // Important for FastAPI
      },
      body: JSON.stringify(data)
    });

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const result = await response.json();
    console.log("Server response:", result);
    alert(result.message);

  } catch (error) {
    console.error("Fetch error:", error);
  }
}

// Call it on page load or button click
sendData();
