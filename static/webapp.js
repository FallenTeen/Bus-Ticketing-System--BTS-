function redirectToLogin() {
    window.location.href = '/loginRender';
}
function cariKeberangkatan(){
    var asal = document.querySelector('#f-asal input').value;
    var tujuan = document.querySelector('#f-tujuan input').value;
    var tanggal = document.querySelector('#f-tanggal-berangkat input').value;

    // Mengubah window.location.href ke endpoint '/formOrder' dengan query string
    window.location.href = '/formOrder?inputAsal=' + encodeURIComponent(asal) + '&inputTujuan=' + encodeURIComponent(tujuan) + '&inputTanggal=' + encodeURIComponent(tanggal);
}

function cariKeberangkatan2(tujuan) {
    var asal = ''; // Tetapkan nilai asal sesuai kebutuhan
    var tanggal = ''; // Tetapkan nilai tanggal sesuai kebutuhan

    // Mengubah window.location.href ke endpoint '/formOrder' dengan query string
    window.location.href = '/formOrder?inputAsal=' + encodeURIComponent(asal) + '&inputTujuan=' + encodeURIComponent(tujuan) + '&inputTanggal=' + encodeURIComponent(tanggal);
}
function showForm(formId) {
    document.getElementById(formId).style.display = 'flex';
}

function hideForm(formId) {
    document.getElementById(formId).style.display = 'none';
}

window.onload = function() {
    showForm('formBuses');
};

function showBusesForm() {
    showForm('formBuses');
    hideForm('formFNB')
}

function showFNBForm() {
    hideForm('formBuses');
    showForm('formFNB');
}

function pesanMakanan(namaMakanan, harga) {
    var idPesanan = prompt("Masukkan ID Tiket Anda:");
    var namapemesan = prompt("Masukkan nama pemesan:");
    var jumlahPesanan = prompt("Masukkan jumlah pesanan:");
  
    if (idPesanan !== null && jumlahPesanan !== null) {
        fetch('/pesan_makanan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                namapemesan: namapemesan,
                idtiket: idPesanan, // Memastikan penggunaan variabel yang benar
                jumlahPesanan: jumlahPesanan,
                nama_makanan: namaMakanan,
                harga: harga
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.message);
            alert(data.message);
        });
    } else {
        alert("Pemesanan dibatalkan.");
    }
}


function bayarmakan() {
    document.getElementById('bayarmakan').style.display = 'block';
    document.getElementById('beli_tiket').style.display = 'none';
}

function buattiket() {
    document.getElementById('bayarmakan').style.display = 'none';
    document.getElementById('beli_tiket').style.display = 'block';
}


$('#datepicker-cashier').prop('disabled', true);
function swapAsalTujuan() {
    var asal = document.getElementById('f-asal');
    var tujuan = document.getElementById('f-tujuan');

    var tempHTML = asal.innerHTML; // Simpan isi f-asal sementara

    // Tukar isi dan tampilan f-asal dan f-tujuan
    asal.innerHTML = tujuan.innerHTML;
    tujuan.innerHTML = tempHTML;
}
