import mysql.connector
import datetime
from mysql.connector import Error
from flask import Flask,session, request,jsonify, render_template, redirect, url_for
from random import randint
from math import ceil
from itertools import zip_longest


app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('login.html')

@app.route('/')
def index():
    return render_template('webapp.html')

@app.route('/loginRender', methods = ['GET'])
def renderLogin():
    return render_template('login.html')


@app.route('/login', methods = ['POST'])
def identifikasiUser():
    username = request.form['username']
    password = request.form['password']

    try:
        if username == 'kasir' and password == 'kasir123':

            return render_template('kasir.html')
        
        elif username == 'manager' and password == '12345678':

            return render_template('manager.html')
        
        else:
            return render_template('loginfail.html')
    except Exception as e:
        print(e)
        return render_template('loginfail.html')
    #kasir
#Lihat Status keberangkatan Start

@app.route('/fetchDataKeberangkatan', methods = ['GET'])
def getListKeberangkatan():
	return render_template('formListKeberangkatan.html')

@app.route('/tampilkanDataKeberangkatan', methods=['GET'])
def get_data_from_db():
    try:
        tanggal = request.args.get('tanggal')  # Menggunakan request.args untuk mendapatkan nilai dari parameter URL
        query = """
        SELECT 
        k.id_keberangkatan, 
        k.id_po, 
        p.nama_po, 
        k.Kelas, 
        k.Tujuan, 
        k.Tanggal_Keberangkatan,
        COUNT(tb.id_tiket) AS total_tiket_terbeli FROM keberangkatan k LEFT JOIN po p ON k.id_po = p.id_po LEFT JOIN tiketterbeli tb ON k.id_keberangkatan = tb.id_keberangkatan
        WHERE k.tanggal_keberangkatan = %s GROUP BY  k.id_keberangkatan, k.id_po, p.nama_po, k.Kelas, k.Tujuan, k.Tanggal_Keberangkatan;
        """

        inser_valuenya = (tanggal,)
        result = runQuery2(query, inser_valuenya)
        
        if result:
            return render_template('keberangkatan.html', data=result)
        else:
            return jsonify({"message": "Data tidak ditemukan"})
    
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/berangkatkan', methods=['POST'])
def hapusId_Keberangkatan():
    try:
        idDihapus = request.args.get('id_diberangkatkan')
        query = "DELETE FROM keberangkatan WHERE id_keberangkatan = %s"
        result = runQuery2(query, (idDihapus,))

        if result:
            # Ambil kembali data setelah penghapusan
            query_select = "SELECT * FROM keberangkatan"
            data_keberangkatan = runQuery(query_select)

            if data_keberangkatan:
                return render_template('keberangkatan.html', data=data_keberangkatan)
            else:
                return jsonify({"message": "Data tidak ditemukan"})
        else:
            return jsonify({"message": "Gagal menghapus data"})
    
    except Exception as e:
        return jsonify({"error": str(e)})
#Lihat Status Keberangkatan End
#INPUT PO STARTTTTTTTTTTTT
@app.route('/fetchFormPo', methods = ['GET'])
def getFormPo():
	return render_template('formPo.html')



@app.route('/inputPo', methods = ['POST'])
def inputPo():
    namaPo = request.form['namaPo']
    tujuan = request.form['tujuan']
    kelas = request.form['kelas']
    jmlKursi = request.form['jmlKursi']
    harga = request.form['harga']
    
    res = runQuery(
        "SELECT * FROM po WHERE nama_po = '{}' AND kelas = '{}' AND tujuan = '{}' AND jumlah_kursi = '{}' AND harga = '{}'".format(
            namaPo, kelas, tujuan, jmlKursi, harga)
    )

    if res:
        return '<h5>PO Tersebut Sudah Ada</h5>'
    IDpo = 0 
    res = None

    if kelas == '--':
        return '<h5>Pilih kelas</h5>'
    IDpo = 0 
    res = None

    while res != []:
        IDpo = randint(0, 696969)
        res = runQuery("SELECT id_po FROM po WHERE id_po = " + str(IDpo))

    res = runQuery("INSERT INTO po VALUES(" + str(IDpo) + ",'" + namaPo + "','" + kelas + "','" + tujuan + "','" + jmlKursi+ "','" + harga +"')")

    if res == []:
        print("Berhasil Menambahkan")
        return '<h4>Berhasil Menambahkan</h4>'\
            '<h6>ID PO: ' + str(IDpo) + '</h6>'
    else:
        print(res)

    return '<h5>Error</h5>'


#INPUT PO END

#Buat Keberangkatan Start



@app.route('/formKeberangkatan', methods=['GET'])
def form_keberangkatan():
    query = "SELECT DISTINCT tujuan FROM po"
    result = runQuery(query)
    tujuan = [row[0] for row in result]

    return render_template('formKeberangkatan.html', tujuan=tujuan)

@app.route('/listPoDenganTujuan', methods=['GET'])
def listPoDenganTujuan():
    tujuanDipilih = request.args.get('tujuanDipilih')  # Mengambil nilai dari URL
    query = "SELECT DISTINCT id_po, nama_po, kelas, tujuan, jumlah_kursi, harga FROM po WHERE tujuan='" + tujuanDipilih + "'"
    res = runQuery(query)
    listPo = res
    return render_template('formListPo.html', listPo=listPo)

@app.route('/berangkatkanPo', methods=['POST'])
def berangkatkanPoDenganId():
    busDiberangkatkan = request.form['busDiberangkatkan']
    tanggalKeberangkatan = request.form['tanggalKeberangkatan']
    id_keberangkatan = randint(0, 696969)
    res = runQuery(
        "SELECT * FROM keberangkatan WHERE id_po = '{}' AND Tanggal_Keberangkatan = '{}'".format(
            busDiberangkatkan, tanggalKeberangkatan)
    )

    if res:
        return '<h5>Keberangkatan PO tersebut sudah ada</h5>'
    res = None

    if res != []:
        id_keberangkatan = randint(0, 696969)
        query_insert = "INSERT INTO keberangkatan (id_keberangkatan, id_po, Tujuan, Tanggal_Keberangkatan, Kelas) "\
                        "SELECT %s, id_po, tujuan, %s, kelas FROM po WHERE id_po = %s"
        values_insert = (id_keberangkatan, tanggalKeberangkatan, busDiberangkatkan)
        runQuery2(query_insert, values_insert)
        return "<h4>Berhasil membuat pemberangkatan.</h4><br><h6>ID Keberangkatan :{}</h6>".format(id_keberangkatan)

#Buat Keberangkatan End
#Kasir Start

@app.route('/getFormTiket', methods=['POST'])
def bukaTiketing():
    pelanggan = request.form['namaPelanggan']

    res = runQuery("SELECT DISTINCT tujuan FROM keberangkatan")
    listKeberangkatan = [item[0] for item in res]

    return render_template('buatTiket.html', namaPelanggan=pelanggan, listKeberangkatan=listKeberangkatan)
#WEBBB START
@app.route('/fetchFormLoginnya', methods = ['GET'])
def getFormLogin():
	return render_template('login.html')

@app.route('/getFormPoTersedia', methods=['POST'])
def bukaFormPoTersedia2():
    tujuanDituju = request.form['tujuanDituju']
    tglDipilih = request.form['tglDipilih']
    pelanggan = request.form['namaPelanggan']

    query = "SELECT keberangkatan.id_keberangkatan, keberangkatan.id_po, po.nama_po, keberangkatan.Tujuan, keberangkatan.Tanggal_Keberangkatan, keberangkatan.Kelas, po.harga FROM keberangkatan JOIN po ON keberangkatan.id_po = po.id_po WHERE keberangkatan.Tujuan = %s AND keberangkatan.Tanggal_Keberangkatan = %s"
    values = (tujuanDituju, tglDipilih)

    listPoNya = runQuery2(query, values)

    return render_template('pilihanPo.html', pelanggan=pelanggan, listPoNya=listPoNya)

@app.route('/getFormPoOrder', methods=['POST'])
def bukaFormPoTersediaOrder():
    asal = request.form['asal']
    tujuan = request.form['tujuan']
    tglDipilih = request.form['tglDipilih']
    pelanggan = request.form['namaPelanggan']
    kelas = request.form['kelas']
    
    query = "SELECT keberangkatan.id_keberangkatan, keberangkatan.id_po, po.nama_po, keberangkatan.Asal, keberangkatan.Tujuan, keberangkatan.Kelas, po.harga FROM keberangkatan JOIN po ON keberangkatan.id_po = po.id_po WHERE keberangkatan.Asal= %s AND keberangkatan.Tujuan= %s AND keberangkatan.Tanggal_Keberangkatan = %s AND keberangkatan.Kelas = %s"
    values = (asal, tujuan, tglDipilih, kelas)

    listPoNya = runQuery2(query, values)

    data_ditemukan = bool(listPoNya)

    if not data_ditemukan:
       return ""
    else:
        return render_template('pilihanPoOrder.html', pelanggan=pelanggan, listPoNya=listPoNya, data_ditemukan=data_ditemukan)

   


@app.route('/tampilKursi', methods=['POST'])
def tampilKursiTersedia():
    id_po = request.form['id_po']
    id_keberangkatan = request.form['id_keberangkatan']

    query_jumlah_kursi = "SELECT COUNT(*) AS jumlah_kursi_terpakai FROM kursi k JOIN tiketTerbeli t ON k.no_kursi = t.noKursi WHERE k.id_po = %s AND t.id_keberangkatan = %s"
    valinsert = (id_po, id_keberangkatan)
    kursiTersisa = runQuery2(query_jumlah_kursi, valinsert)

    query_kursi_tersedia = """
        SELECT k.kolom, k.baris, k.no_kursi
        FROM kursi k 
        LEFT JOIN tiketTerbeli t ON k.no_kursi = t.noKursi 
        WHERE k.id_po = %s AND (t.id_keberangkatan != %s OR t.id_keberangkatan IS NULL)
    """
    query_insert = (id_po, id_keberangkatan)

    kursi_tersedia = runQuery2(query_kursi_tersedia, query_insert)

    kolom = [row[0] for row in kursi_tersedia]
    baris = [row[1] for row in kursi_tersedia]
    noKursi = [row[2] for row in kursi_tersedia]

    query_kursi_terbeli = """
        SELECT k.kolom, k.baris, k.no_kursi
        FROM kursi k 
        INNER JOIN tiketTerbeli t ON k.no_kursi = t.noKursi 
        WHERE k.id_po = %s AND t.id_keberangkatan = %s
    """
    valinsert = (id_po, id_keberangkatan)
    kursi_terbeli = runQuery2(query_kursi_terbeli, valinsert)

    return render_template('pilKursi.html', kursiTersisa=kursiTersisa, kursi_tersedia=kursi_tersedia, kolom=kolom, baris=baris, noKursi=noKursi, kursi_terbeli=kursi_terbeli)

@app.route('/tampilKursiOrder', methods=['POST'])
def tampilKursiTersediaOrder():
    id_po = request.form['id_po']
    id_keberangkatan = request.form['id_keberangkatan']

    query_kelas = "SELECT kelas FROM po WHERE id_po = %s"
    valinsert0 = (id_po,)
    kelass = runQuery2(query_kelas, valinsert0)
    
    query_jumlah_kursi = "SELECT COUNT(*) AS jumlah_kursi_terpakai FROM kursi k JOIN tiketTerbeli t ON k.no_kursi = t.noKursi WHERE k.id_po = %s AND t.id_keberangkatan = %s"
    valinsert = (id_po, id_keberangkatan)
    kursiTersisa = runQuery2(query_jumlah_kursi, valinsert)

    query_kursi_tersedia = """
        SELECT k.kolom, k.baris, k.no_kursi 
        FROM kursi k 
        LEFT JOIN tiketTerbeli t ON k.no_kursi = t.noKursi 
        WHERE k.id_po = %s AND (t.id_keberangkatan != %s OR t.id_keberangkatan IS NULL)
    """
    query_insert = (id_po, id_keberangkatan)
    kursi_tersedia = runQuery2(query_kursi_tersedia, query_insert)

    kolom = [row[0] for row in kursi_tersedia]
    baris = [row[1] for row in kursi_tersedia]
    noKursi = [row[2] for row in kursi_tersedia]

    query_kursi_terbeli = """
        SELECT k.kolom, k.baris, k.no_kursi
        FROM kursi k 
        INNER JOIN tiketTerbeli t ON k.no_kursi = t.noKursi 
        WHERE k.id_po = %s AND t.id_keberangkatan = %s
    """
    valinsert = (id_po, id_keberangkatan)
    kursi_terbeli = runQuery2(query_kursi_terbeli, valinsert)

    return render_template('pilKursiOrder.html', kelass=kelass, kursiTersisa=kursiTersisa, kursi_tersedia=kursi_tersedia, kolom=kolom, baris=baris, noKursi=noKursi, kursi_terbeli=kursi_terbeli)

@app.route('/buatTiket', methods=['POST'])
def buatUploadanTiket():
    try:
        # Retrieve data from the request
        namaPelanggan = request.form.get('namaPelanggan')
        id_keberangkatan = request.form.get('id_keberangkatan')
        tujuan = request.form.get('tujuan')
        tanggal = request.form.get('tanggal_keberangkatan')
        nama_po = request.form.get('nama_po')
        noKursi = request.form.get('noKursi')
        kelas = request.form.get('kelas')
         
        randIdTiket = randint(0, 6969669)
        
        queryInsertnya = "INSERT INTO tiketterbeli"\
            "(id_tiket, id_keberangkatan, namaPenumpang, tujuan, tanggal_keberangkatan, po, noKursi, kelas) "\
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values_to_insert = (randIdTiket, id_keberangkatan, namaPelanggan, tujuan, tanggal, nama_po, noKursi, kelas)

        # Execute the query using a function like runQuery3
        result = runQuery2(queryInsertnya, values_to_insert)
        html_content = '<h4>Berhasil Membuat Tiket.</h4>' \
               '<h3>ID Tiket anda adalah: ' + str(randIdTiket) + '</h3>' \
               '<p>ID Keberangkatan: ' + str(id_keberangkatan) + '</p>' \
               '<p>Nama Pelanggan: ' + str(namaPelanggan) + '</p>' \
               '<p>Tujuan: ' + str(tujuan) + '</p>' \
               '<p>Tanggal: ' + str(tanggal) + '</p>' \
               '<p>Nama PO: ' + str(nama_po) + '</p>' \
               '<p>No Kursi: ' + str(noKursi) + '</p>' \
               '<p>Kelas: ' + str(kelas) + '</p>' \
               '<button onclick="login()">OK</button>'
        
        if result:
            return render_template('struk.html', hasil = html_content)
    except Exception as e:
        # Handle exceptions appropriately, perhaps log the error
        print("Exception occurred:", e)

@app.route('/cekKursi', methods=['POSt'])
def cekkursi1():
    try:
        id_po = request.form.get('id_po')

        queryselect = "SELECT jumlah_kursi FROM po WHERE id_po = %s"
        insertan = (id_po,)
        result = runQuery2(queryselect, insertan)
        return jsonify({'result': result})
    except Exception as e:
        # Handle exceptions appropriately, perhaps log the error
        print("Exception occurred:", e)

@app.route('/buatTiketOrder', methods=['POST'])
def buatUploadanTiketOrder():
    try:
        # Retrieve data from the request
        namaPelanggan = request.form.get('namaPelanggan')
        id_keberangkatan = request.form.get('id_keberangkatan')
        tujuan = request.form.get('tujuan')
        tanggal = request.form.get('tanggal_keberangkatan')
        nama_po = request.form.get('nama_po')
        noKursi = request.form.get('noKursi')
        kelas = request.form.get('kelas')
         
        randIdTiket = randint(0, 6969669)
        
        queryInsertnya = "INSERT INTO tiketterbeli"\
            "(id_tiket, id_keberangkatan, namaPenumpang, tujuan, tanggal_keberangkatan, po, noKursi, kelas) "\
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values_to_insert = (randIdTiket, id_keberangkatan, namaPelanggan, tujuan, tanggal, nama_po, noKursi, kelas)
        result = runQuery2(queryInsertnya, values_to_insert)
        html_content = '<h4>Berhasil Membuat Tiket.</h4>' \
               '<h3>ID Tiket anda adalah: ' + str(randIdTiket) + '</h3>' \
               '<p>ID Keberangkatan: ' + str(id_keberangkatan) + '</p>' \
               '<p>Nama Pelanggan: ' + str(namaPelanggan) + '</p>' \
               '<p>Tujuan: ' + str(tujuan) + '</p>' \
               '<p>Tanggal: ' + str(tanggal) + '</p>' \
               '<p>Nama PO: ' + str(nama_po) + '</p>' \
               '<p>No Kursi: ' + str(noKursi) + '</p>' \
               '<p>Kelas: ' + str(kelas) + '</p>' \
               '<button onclick="location.reload()">OK</button>'
        
        if result:
            return render_template('struk2.html', hasil = html_content)
    except Exception as e:
        # Handle exceptions appropriately, perhaps log the error
        print("Exception occurred:", e)
#Ubah PO Start
 
@app.route('/fetchUbahPo', methods=['GET'])
def fetchPo():
    try:
        query = "SELECT id_po, nama_po, kelas, tujuan, jumlah_kursi, harga FROM po"
        hasilQuery = runQuery(query)
        id_po = [row[0] for row in hasilQuery] 
        nama_po = [row[1] for row in hasilQuery] 
        kelas = [row[2] for row in hasilQuery]
        tujuan = [row[3] for row in hasilQuery]
        jumlah_kursi = [row[4] for row in hasilQuery]  
        harga = [row[5] for row in hasilQuery]

        return render_template('UbahPo.html', data=zip(id_po, nama_po, kelas, tujuan, jumlah_kursi, harga))

        
    except Exception as e:
        # Handle exceptions appropriately, perhaps log the error
        print("Exception occurred:", e)


@app.route('/fetchUbahPoIni', methods=['POST'])
def fetchUbahPoIniSekarang():
    try:
        id_po = request.form.get('id_po')
        nama_po = request.form.get('nama_po')
        kelas = request.form.get('kelas')
        tujuan = request.form.get('tujuan')
        jumlah_kursi = request.form.get('jumlah_kursi')
        harga = request.form.get('harga')

        return render_template('editPo.html', id_po=id_po, nama_po=nama_po, kelas=kelas, tujuan=tujuan, jumlah_kursi=jumlah_kursi, harga=harga)

    except Exception as e:
        print("Error occurred:", str(e))

@app.route('/updatePoIniDenganNilaiYangBaru', methods=['POST'])
def updatePoIni():
    try:
        id_po = request.form.get('id_po')
        nama_po = request.form.get('nama_po')
        kelas = request.form.get('kelas')
        tujuan = request.form.get('tujuan')
        jumlah_kursi = request.form.get('jumlah_kursi')
        harga = request.form.get('harga')

        print("id_po:", id_po)
        print("nama_po:", nama_po)
        print("kelas:", kelas)
        print("tujuan:", tujuan)
        print("jumlah_kursi:", jumlah_kursi)
        print("harga:", harga)
    
        updateQuery = "UPDATE po SET nama_po = %s, kelas = %s, tujuan = %s, jumlah_kursi = %s, harga = %s WHERE id_po = %s"
        insertValue = (nama_po, kelas, tujuan, jumlah_kursi, harga, id_po)
        runQuery2(updateQuery, insertValue)

        hasil = runQuery("SELECT * FROM po WHERE id_po='"+id_po+"'")
        print(hasil)

        return '<h4>Berhasil Update Po</h4>'
    except Exception as e:
        print("Error occurred:", str(e))
        return '<h4>Gagal melakukan update Po</h4>'


#Ubah PO End
        
@app.route('/formOrder', methods=['GET'])
def render_order():
    
    asal = request.args.get('inputAsal', None)
    tujuan = request.args.get('inputTujuan', None)
    tanggal = request.args.get('inputTanggal', None)
    
    return render_template('FormOrder.html', inputAsal=asal, inputTujuan=tujuan, inputTanggal=tanggal)

@app.route('/pesan_makanan', methods=['POST'])
def pesan_makanan():
    id_bayar = randint(0, 150)
    namapemesan = request.json.get('namapemesan')
    idtiket = request.json.get('idtiket')
    nama_makanan = request.json.get('nama_makanan')
    jumlahpesanan = int(request.json.get('jumlahPesanan'))  # Ubah ke tipe data numerik
    harga = int(request.json.get('harga'))  # Ubah ke tipe data numerik
    totalharga = harga * jumlahpesanan

    # Sesuaikan struktur query sesuai dengan kolom di tabel Anda
    pesan = "INSERT INTO pesanan VALUES (%s, %s, %s, %s, %s,%s, 'unpaid')"
    insertan = (id_bayar, idtiket, namapemesan, nama_makanan, jumlahpesanan, totalharga)
    result = runQuery2(pesan, insertan)

    print(result)
    print(f"Pesanan: {nama_makanan}, Harga: {harga}")

    return jsonify({
        "message": f"Pesanan berhasil diterima! Silahkan lakukan pembayaran. ID pembayaran = {id_bayar}\
            total tagihan : {totalharga}"
    })
    



# @app.route('/uploadTiket', methods=['POST'])
# def cekDanInputTiket(namaPelanggan, id_keberangkatan, tujuan, tanggal, kelas):
#     try:
#         randIdTiket = randint(0, 6969669)

#         # Query untuk memeriksa ketersediaan kursi dengan kelas yang sama
#         query_check_available_seat = "SELECT COUNT(*) FROM kursi "\
#                                      "JOIN keberangkatan ON kursi.id_po = keberangkatan.id_po "\
#                                      "WHERE keb.id_keberangkatan = %s AND k.kelas = %s"
#         values_available_seat = (id_keberangkatan, kelas)

#         result_available_seat = runQuery2(query_check_available_seat, values_available_seat)

#         if result_available_seat and result_available_seat[0][0] > 0:
#             # Jika ada kursi tersedia, lakukan input data ke tabel tiketterbeli
#             query_insert_to_tiketterbeli = "INSERT INTO tiketterbeli (id_tiket, id_keberangkatan, namaPenumpang, tujuan, tanggal_keberangkatan) "\
#                                            "VALUES (%s, %s, %s, %s, %s)"
#             values_insert_to_tiketterbeli = (randIdTiket, id_keberangkatan, namaPelanggan, tujuan, tanggal)

#             runQuery2(query_insert_to_tiketterbeli, values_insert_to_tiketterbeli)
#             return f'<h4>Berhasil menambahkan.</h4><br><h5>ID Tiket : {randIdTiket}</h5>'
#         else:
#             return '<h4>Gagal menambahkan tiket. Kursi tidak tersedia.</h4>'

#     except Exception as e:
#         return f'Error: {str(e)}'




#Kasir End
# Makananan START
@app.route('/get_data_makanan', methods =['GET'])
def get_data_makanan():
    # Query yang ingin dieksekusi untuk mengambil data dari database
    query = "SELECT * FROM pesanan"  # Ganti dengan query yang sesuai
    data = runQuery(query)
    id_pesanan = [row[0] for row in data] 
    id_tiket = [row[1] for row in data] 
    nama_pemesan = [row[2] for row in data]
    makanan = [row[3] for row in data]
    jumlah = [row[4] for row in data]  
    tagihan = [row[5] for row in data]  
    status = [row[6] for row in data]
    return render_template('pesanan.html',id_pesanan=id_pesanan, id_tiket=id_tiket,nama_pemesan=nama_pemesan,makanan=makanan,jumlah=jumlah, tagihan=tagihan, status=status)

@app.route('/update_status', methods=['POST'])
def update_status():
    id_pesanan = request.json.get('id_pesanan')
    
    # Query untuk melakukan UPDATE nilai kolom status pada tabel dengan id_tiket tertentu
    query = f"UPDATE pesanan SET status = 'paid' WHERE id_pesanan = '{id_pesanan}'"
    
    # Jalankan query ke database
    hasil = runQuery(query)  # Kamu perlu memastikan bahwa fungsi runQuery sesuai dengan cara koneksi dan eksekusi query di database kamu
    if hasil:
        return jsonify({'success': True, 'message': 'Pesanan berhasil dibayar.'}), 200
    else:
        return jsonify({'success': False, 'message': 'Gagal membayar pesanan.'}), 400


# Makanan END
def runQuery2(query, values=None):
    try:
        db = mysql.connector.connect(
            host='localhost',
            database='dbbis',
            user='root',
            password='')
        
        if db.is_connected():
            print("Berhasil Terkoneksi Dengan Database", query)
            cursor = db.cursor(buffered=True)
            if values:
                cursor.execute(query, values)  # Eksekusi query dengan values yang diterima
            else:
                cursor.execute(query)
            
            # Check if it's an INSERT or any other query
            if query.lower().startswith("insert"):
                db.commit()
                return True  # Return True for successful INSERT
            else:
                res = cursor.fetchall()
                return res  # Return result for other queries (SELECT, etc.)
    except Exception as e:
        print("Error:", e)
        return False  # Return False for failure
    
    finally:
        db.close()

    print("Gagal Terkoneksi Ke Database")
    return None

# def runQuery2(query, values=None):
#     try:
#         db = mysql.connector.connect(
#             host='localhost',
#             database='dbbis',
#             user='root',
#             password='')
        
#         if db.is_connected():
#             print("Berhasil Terkoneksi Dengan Database", query)
#             cursor = db.cursor(buffered=True)
#             if values:
#                 cursor.execute(query, values)  # Eksekusi query dengan values yang diterima
#             else:
#                 cursor.execute(query)
#             db.commit()
#             res = None
#             try:
#                 res = cursor.fetchall()
#             except Exception as e:
#                 print("Error", e)
#                 return []
#             return res
#     except Exception as e:
#         print(e)
#         return e
    
#     finally:
#         db.close()

#     print("Gagal Terkoneksi Ke Database")
#     return None

def runQuery(query):
    try:
        db = mysql.connector.connect(
            host='localhost',
            database='dbbis',
            user='root',
            password='')
        
        if db.is_connected():
            print("Berhasil Terkoneksi Dengan Database", query)
            cursor = db.cursor(buffered = True)
            cursor.execute(query)
            db.commit()
            res = None
            try:
                res = cursor.fetchall()
            except Exception as e:
                print("Error", e)
                return []
            return res
    except Exception as e:
        print(e)
        return e
    
    finally:
        db.close()

    print("Gagal Terkoneksi Ke Database")
    return None

if __name__ == "__main__":
    app.run(host='0.0.0.0')

