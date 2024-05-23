var username = null;
var password = null;
var tanggal = null;
var idBus = null;
var kelas = null;
var noKursi = null;
var keberangkatan = null;
var tujuan = null;
var harga = null;
var piltujuan = null;
var global_id_keberangkatan;
var global_id_po;
var global_tujuan;
var global_tanggal_keberangkatan;
var global_kelas;
var global_nama_po;
var global_harga;
function login(){
    if(username === null){
        username = $("[name='username']")[0].value;
        password = $("[name='password']")[0].value;
    }
    var form = {
        'username' : username,
        'password' : password
    }
    $.ajax({
        type : 'POST',
        url: '/login',
        data: form,
        success: function(response){
            $('.module').html(response);
            $('.module').addClass('module-after-login');
            $('.login-header').addClass('after-login');
            $('.tanggal_kasir').pickadate({
                tgl : new Date(),
                formatSubmit: 'yyyy/mm/dd',
                hiddenName: true,
                onSet: function( event ) {
                    if ( event.select ) {
                        $('#datepicker-cashier').prop('disabled', true);
                        listKeberangkatanPada(this.get('select', 'yyyy/mm/dd'));
                    }
                }
            })
        }
    })
    
}

//Info Keberangkatan Start

function listKeberangkatan() {
    $('#options button').prop('disabled', true);
	$.ajax({
		type: 'GET',
		url: '/fetchDataKeberangkatan',
		success: function(response){
			$('#manager-dynamic-1').html(response);
		}
	});
}
function berangkatkanIdIni(id){
    $.ajax({
		type: 'POST',
		url: '/berangkatkan',
        data:{
            'id_diberangkatkan' : id
        },
		success: function(response){
			$('#manager-dynamic-2').html(response);
		}
	}); 
}
//Info keberangkatan end

//Input PO Start
function inputPo(){
	$('#options button').prop('disabled', true);
	$.ajax({
		type: 'GET',
		url: '/fetchFormPo',
		success: function(response){
			$('#manager-dynamic-1').html(response);
		}
	});
}
function uploadPo(){
	namaPo = $('[name="namaPo"]')[0].value;
	tujuan = $('[name="tujuan"]')[0].value;
	kelas = $('[name="kelas"]')[0].value;
    jmlKursi = $('[name="jmlKursi"]')[0].value;
    harga = $('[name="harga"]')[0].value;
		$.ajax({
			type: 'POST',
			url: '/inputPo',
			data: {
				'namaPo' : namaPo,
				'tujuan' : tujuan,
				'kelas' : kelas,
                'jmlKursi' : jmlKursi,
                'harga' : harga
			},
			success: function(response){
				$('#manager-dynamic-2').html(response);
			}
		});
	}
//Input PO End
//Buat Keberangkatan Start
function buatKeberangkatan() {
    $('#options button').prop('disabled', true);
    $.ajax({
        type: 'GET',  
        url: '/formKeberangkatan',
        success: function(response){
            $('#manager-dynamic-2').html(response);

            // Menginisialisasi pickadate pada elemen input dengan class "datepicker-berangkatkan"
            $('.datepicker-berangkatkan').pickadate({
                format: 'yyyy/mm/dd',
                min: new Date(),
                selectYears: true,
                selectMonths: true,
                closeOnSelect: true,
                onClose: function() {
                    var selectedDate = this.get();
                    if (selectedDate) {
                     $('#datepicker-cashier').prop('disabled', true);
                     berangkatkanPadaTanggal(this.get('select', 'yyyy/mm/dd'));
                    }
                }
            });
        }
    });
}

function tampilPo(){
    var tujuanDipilih = $('#cekpotersedia').val(); // Menggunakan jQuery untuk mengambil nilai dropdown

    $.ajax({
        type: 'GET',
        url: '/listPoDenganTujuan',
        data:{
            'tujuanDipilih':tujuanDipilih
        },
        success: function(response){
            $('#manager-dynamic-3').html(response);
        }
    });
}


function berangkatkan(id) {
    var busDiberangkatkan = id;
    var tanggalKeberangkatan = document.getElementById('tanggalKeberangkatan').value;
    $.ajax({
        type: 'POST',
        url: '/berangkatkanPo',
        data:{
            'busDiberangkatkan' : busDiberangkatkan,
            'tanggalKeberangkatan': tanggalKeberangkatan
        },
        success: function(response){
            $('#manager-dynamic-4').html(response); // Mengubah isi elemen dengan ID 'manager-dynamic-4' dengan response dari server
        }
    });
}
//Buat Keberangkatan End

//Buat Tiket Start
function bukaTiket(namaPelanggan){
    var namaPelanggan = document.getElementById('namaPelanggan').value.toUpperCase();
    $.ajax({
        type: 'POST',
        url: '/getFormTiket',
        data: {
            'namaPelanggan': namaPelanggan
        },
        success: function(response){
            $('#namaPelanggan').hide();
            $('#tombolNama').hide();
            $('#tujuan').html(response);
        }
    })
    // $.ajax({
    //     type: 'POST',
    //     url: '/buatTiket',
    //     data: {
    //         'namaPelanggan': namaPelanggan
    //     }
    // });
}

function getListPo() {
    var tujuanYangDipilih = document.getElementById('pilihTujuan').value.toLowerCase();
    var tanggalKeberangkatan = document.getElementById('cekPoDenganTanggal').value;
    var namaPelanggan = document.getElementById('namaPelanggan').value; // Pastikan variabel ini tersedia
    global_nama_pelanggan = document.getElementById('namaPelanggan').value;

    $.ajax({
        type: 'POST',
        url: '/getFormPoTersedia',
        data: {
            'tujuanDituju': tujuanYangDipilih,
            'tglDipilih': tanggalKeberangkatan,
            'namaPelanggan': namaPelanggan
        },
        success: function(response){
            $('#po_tersedia').html(response); // Pastikan ID yang diakses adalah 'po_tersedia'
        }
    });
}
function cekJumlahKursi(id_po) {
    fetch('/cekKursi', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'id_po': id_po,
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Menampilkan hasil query sebagai alert
        alert('Jumlah Kursi Tersedia adalah : ' + data.result);
    })
    .catch(error => console.error('Error:', error));

}
function tampilkanKursiTersedia(id_keberangkatan, id_po, nama_po, tujuan, tanggal_keberangkatan, kelas, harga){
    id_keberangkatan = id_keberangkatan;
    global_id_keberangkatan = id_keberangkatan;
    var id_po = id_po;
    global_id_po = id_po
    var tujuan = tujuan;
    global_tujuan = tujuan;
    var tanggal_keberangkatan = tanggal_keberangkatan;
    global_tanggal_keberangkatan = tanggal_keberangkatan;
    var kelas = kelas;
    global_kelas = kelas;
    var nama_po = nama_po;
    global_nama_po = nama_po;
    var harga = harga;
    global_harga = harga;

    $.ajax({
        type: 'POST',
        url: '/tampilKursi',
        data:{
            'id_keberangkatan' : id_keberangkatan,
            'id_po' : id_po
        }, 
        success: function(response){
            $('#tampilKursi').html(response)
        }
    });
}

var kursiTerpilih = []; // Variabel untuk menyimpan kursi yang dipilih

function inputKursi(noKursi) {
    if (!kursiTerpilih.includes(noKursi)) {
        kursiTerpilih.push(noKursi);
        
    }
    // Tidak ada alert di sini
}

function tampilkanKursiTersediaOrder(id_keberangkatan, id_po, nama_po, tujuan, tanggal_keberangkatan, kelas, harga){
    id_keberangkatan = id_keberangkatan;
    global_id_keberangkatan = id_keberangkatan;
    var id_po = id_po;
    global_id_po = id_po
    var tujuan = tujuan;
    global_tujuan = tujuan;
    var tanggal_keberangkatan = tanggal_keberangkatan;
    global_tanggal_keberangkatan = tanggal_keberangkatan;
    var kelas = kelas;
    global_kelas = kelas;
    var nama_po = nama_po;
    global_nama_po = nama_po;
    var harga = harga;
    global_harga = harga;
    
    $.ajax({
        type: 'POST',
        url: '/tampilKursiOrder',
        data:{
            'id_keberangkatan' : id_keberangkatan,
            'id_po' : id_po
        }, 
        success: function(response){
            var newDiv = $('<div>'); // Membuat elemen div baru
            newDiv.html(response); // Mengisi konten baru ke dalam elemen div

            // Menambahkan konten baru ke dalam newContent tanpa menggantikan yang sudah ada
            $('#newContent').append(newDiv); 

            $('#newSection').show(); // Menampilkan newSection
        }
    });
}

function konfirmasiData() {
    var namaPelanggan = global_nama_pelanggan;
    var id_keberangkatan = global_id_keberangkatan;
    var id_po = global_id_po;
    var tujuan = global_tujuan;
    var tanggal_keberangkatan = global_tanggal_keberangkatan;
    var kelas = global_kelas;
    var nama_po = global_nama_po;
    // var pesan = "Data untuk dikirim: \n" +
    // "Nama Pelanggan: " + namaPelanggan + "\n" +
    // "ID Keberangkatan: " + id_keberangkatan + "\n" +
    // "ID PO: " + id_po + "\n" +
    // "Tujuan: " + tujuan + "\n" +
    // "Tanggal Keberangkatan: " + tanggal_keberangkatan + "\n" +
    // "Kelas: " + kelas + "\n" +
    // "Nama PO: "+ nama_po +"\n" +
    // "Kursi yang dipilih: " + kursiTerpilih.join(', ');

    // alert(pesan);
    
    $.ajax({
        type: 'POST',
        url: '/buatTiket',
        data: {
            'namaPelanggan': namaPelanggan,
            'id_keberangkatan': id_keberangkatan,
            'nama_po': nama_po,
            'id_po': id_po,
            'tujuan': tujuan,
            'tanggal_keberangkatan': tanggal_keberangkatan,
            'kelas': kelas,
            'noKursi': kursiTerpilih.join(', ')
        },
        success: function(response) {
            $('.module').html(response);
            $('.module').addClass('module-after-login');
            $('.login-header').addClass('after-login');
    
            // Menambahkan event click pada tombol reset untuk memanggil fungsi login()
            $('#resetButton').on('click', function() {
                login(); // Memanggil fungsi login() saat tombol reset diklik
            });
        }
    });
}

function konfirmasiDataOrder() {
    var namaPelanggan = document.getElementById('namaPelanggan').value.toLowerCase();
    var id_keberangkatan = global_id_keberangkatan;
    var id_po = global_id_po;
    var tujuan = global_tujuan;
    var tanggal_keberangkatan = global_tanggal_keberangkatan;
    var kelas = global_kelas;
    var nama_po = global_nama_po;
    
    
    // var pesan = "Data untuk dikirim: \n" +
    // "Nama Pelanggan: " + namaPelanggan + "\n" +
    // "ID Keberangkatan: " + id_keberangkatan + "\n" +
    // "ID PO: " + id_po + "\n" +
    // "Tujuan: " + tujuan + "\n" +
    // "Tanggal Keberangkatan: " + tanggal_keberangkatan + "\n" +
    // "Kelas: " + kelas + "\n" +
    // "Nama PO: "+ nama_po +"\n" +
    // "Kursi yang dipilih: " + kursiTerpilih.join(', ');

    // alert(pesan);
    
    $.ajax({
        type: 'POST',
        url: '/buatTiketOrder',
        data: {
            'namaPelanggan': namaPelanggan,
            'id_keberangkatan': id_keberangkatan,
            'nama_po': nama_po,
            'id_po': id_po,
            'tujuan': tujuan,
            'tanggal_keberangkatan': tanggal_keberangkatan,
            'kelas': kelas,
            'noKursi': kursiTerpilih.join(', ')
        },
        success: function(response) {
            $('#newSection').html(response); // Mengganti isi div dengan struk.html
            $('#newSection').show(); // Menampilkan div yang sebelumnya tersembunyi
        }
    });
}

//UBAH PO START
function ubahPo(){
    $('#options button').prop('disabled', true);
	$.ajax({
		type: 'GET',
		url: '/fetchUbahPo',
		success: function(response){
			$('#manager-dynamic-1').html(response);
		}
	});
}

function ubahPoIni(id_po, nama_po, kelas, tujuan, jumlah_kursi, harga){
    var id_po = id_po
    var nama_po = nama_po
    var kelas = kelas
    var tujuan = tujuan
    var jumlah_kursi = jumlah_kursi
    var harga = harga
    $('#options button').prop('disabled', true);
	$.ajax({
		type: 'POST',
		url: '/fetchUbahPoIni',
        data:{
            'id_po' : id_po,
            'nama_po' : nama_po,
            'kelas' : kelas,
            'tujuan' : tujuan,
            'jumlah_kursi' : jumlah_kursi,
            'harga' : harga
        },
		success: function(response){
			$('#manager-dynamic-1').html(response);
		}
	});
}

function updatePoIni() {
    var id_po = document.getElementById("id_po").value;
    var nama_po = document.getElementById("nama_po").value;
    var kelas = document.getElementById("kelas").value;
    var tujuan = document.getElementById("tujuan").value;
    var jumlah_kursi = document.getElementById("jumlah_kursi").value;
    var harga = document.getElementById("harga").value;

    $.ajax({
        type: 'POST',
        url: '/updatePoIniDenganNilaiYangBaru',
        data: {
            'id_po': id_po,
            'nama_po': nama_po,
            'kelas': kelas,
            'tujuan': tujuan,
            'jumlah_kursi': jumlah_kursi,
            'harga': harga
        },
        success: function (response) {
            $('#manager-dynamic-1').html(response);
        }
    });
}

//UBAH PO END



    
    // // Menggunakan objek untuk menyimpan data yang akan dikirim
    // var data = {
    //     namaPelanggan: namaPelanggan,
    //     kursiTerpilih: kursiTerpilih,

    // };

    // // Mengirim data ke backend menggunakan AJAX
    // fetch('/buatTiket', {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json',
    //     },
    //     body: JSON.stringify(data)
    // })
    // .then(response => response.json())
    // .then(data => {
    //     // Tindakan yang akan diambil setelah mendapat respons dari server
    //     console.log('Respon dari server:', data);
    //     // Misalnya, menampilkan pesan sukses atau melakukan tindakan lainnya
    // })
    // .catch((error) => {
    //     console.error('Error:', error);
    // });
//}

// function inputKursi(noKursi) {
//     var noKursi = noKursi
//     alert (noKursi);
//     $.ajax({
//         type: 'POST',
//         url: '/buatTiket',
//         daya:{
//             'noKursi' : noKursi,
//             'id_po' : id_po
//         },
//         success: function(response){
//             $('#konfirmasi').html(response)
//         }
//     })
// } 



// function buatTiket(noKursi) {
//     var namaPelanggan = document.getElementById('namaPelanggan').value.toUpperCase();
//     var id_keberangkatan = request.form['id_keberangkatan']
//     var tujuan =  document.getElementById('pilihTujuan').value.toLowerCase();
//     var tanggal_keberangkatan = request.form['tanggal_keberangkatan']
//     var kelas = request.form['kelas']
//     var noKursi = noKursi
    
//     $.ajax({
//         type: 'POST',
//         url: '/buatTiket', // Sesuaikan dengan URL endpoint yang benar
//         data: {
//             'namaPelanggan' : namaPelanggan,
//             'id_keberangkatan' : id_keberangkatan,
//             'tujuan' : tujuan,
//             'tanggal_keberangkatan' : tanggal_keberangkatan,
//             'noKursi': noKursi,
//             'kelas' : kelas
            
//         },
//         success: function(response) {
//             // Tindakan yang diambil ketika permintaan berhasil
//             console.log(response); // Tampilkan respons dari server jika diperlukan
//         },
//         error: function(xhr, status, error) {
//             // Tindakan yang diambil jika terjadi kesalahan
//             console.error(xhr.responseText); // Tampilkan pesan kesalahan dari server jika diperlukan
//         }
//     });
// }







// Fungsi untuk menampilkan pilihan tanggal dari PO yang dipilih
function poTersediaOrder() {
    var namaPelanggan = document.getElementById('namaPelanggan').value;
    var asal = document.getElementById('f-asal').value;
    var tujuan = document.getElementById('f-tujuan').value;
    var tanggalKeberangkatan = document.getElementById('f-tanggal-berangkat').value;
    var kelas = document.getElementById('f-kelas').value;

    $.ajax({
        type: 'POST',
        url: '/getFormPoOrder',
        data: {
            'tujuan': tujuan,
            'tglDipilih': tanggalKeberangkatan,
            'namaPelanggan': namaPelanggan,
            'asal': asal,
            'kelas': kelas
        },
        success: function(response) {
            if (response.trim() !== "") {
                document.getElementById('newContent').innerHTML = '';
                var newDiv = document.createElement("div");
                newDiv.innerHTML = response;
                document.getElementById('newContent').appendChild(newDiv);
                document.getElementById('newSection').style.display = 'block';
                document.getElementById('newSection').scrollIntoView({
                    behavior: 'smooth'
                });
            } else {
                alert("Keberangkatan tersebut tidak tersedia");
            }
        },
        error: function(error) {
            // Menampilkan pesan error di console jika terjadi kesalahan pada request
            console.log("Error:", error);
            // Menghandle error, bisa menampilkan pesan kepada user atau melakukan tindakan tertentu
        }
    });
}


