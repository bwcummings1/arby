setInterval(() => {
    fetch('/api/arbitrage')
        .then(response => response.json())
        .then(data => {
            let table = document.querySelector('table');
            table.innerHTML = "<tr><th>Event</th><th>Stake</th><th>Odds</th><th>Account</th><th>Status</th></tr>";
            data.forEach(bet => {
                let row = `<tr>
                    <td>${bet[1]}</td>
                    <td>$${bet[2]}</td>
                    <td>${bet[3]}</td>
                    <td>${bet[4]}</td>
                    <td>Pending</td>
                </tr>`;
                table.innerHTML += row;
            });
        });
}, 5000);
