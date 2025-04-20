function buscarClt() {
    const input = document.getElementById('buscarClt');
    const filter = input.value.toUpperCase();
    const rows2 = document.getElementById('corpoTabela').getElementsByTagName('tr');
    
    for (let i = 0; i < rows2.length; i++) {
        const cells = rows2[i].getElementsByTagName('td');
        if (cells.length > 0) {
            const nameCell = cells[1]; // Ajuste para a coluna "Nome"
            if (nameCell) {
                const txtValue = nameCell.textContent || nameCell.innerText;
                rows2[i].style.display = txtValue.toUpperCase().indexOf(filter) > -1 ? '' : 'none';
            }
        }
    }
}