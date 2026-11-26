async function getData() {
    const response = await fetch(
        "リンク"
    );

    const data = await response.json();

    console.log(data.message);
}

getData();