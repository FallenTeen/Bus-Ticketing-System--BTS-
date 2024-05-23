-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 08, 2024 at 12:50 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbbis`
--
CREATE DATABASE IF NOT EXISTS `dbbis` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `dbbis`;

-- --------------------------------------------------------

--
-- Table structure for table `harga`
--

DROP TABLE IF EXISTS `harga`;
CREATE TABLE `harga` (
  `id_harga` int(11) NOT NULL,
  `id_po` int(11) DEFAULT NULL,
  `harga` decimal(10,2) DEFAULT NULL,
  `kelas_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `keberangkatan`
--

DROP TABLE IF EXISTS `keberangkatan`;
CREATE TABLE `keberangkatan` (
  `id_keberangkatan` int(11) NOT NULL,
  `id_po` int(11) DEFAULT NULL,
  `Tujuan` varchar(255) DEFAULT NULL,
  `Tanggal_Keberangkatan` date DEFAULT NULL,
  `Kelas` varchar(50) DEFAULT NULL,
  `Asal` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `keberangkatan`
--

INSERT INTO `keberangkatan` (`id_keberangkatan`, `id_po`, `Tujuan`, `Tanggal_Keberangkatan`, `Kelas`, `Asal`) VALUES
(18151, 665548, 'Karangklesem', '2023-12-11', 'Ekonomi', 'Purbalingga'),
(44811, 240968, 'Purbalingga', '2023-12-15', 'Ekonomi', 'Kebumen'),
(93330, 665548, 'Karangklesem', '2023-12-12', 'Ekonomi', 'Brebes'),
(110978, 54524, 'Karangmalang', '2023-12-12', 'Eksekutif', 'Karangsalam'),
(415913, 542491, 'Jakarta', '2023-12-13', 'Eksekutif', 'Karanganyar'),
(488843, 542491, 'Jakarta', '2023-12-14', 'Eksekutif', 'Bandung'),
(667310, 542491, 'Jakarta', '2023-12-15', 'Eksekutif', 'Bandung');

-- --------------------------------------------------------

--
-- Table structure for table `kelas`
--

DROP TABLE IF EXISTS `kelas`;
CREATE TABLE `kelas` (
  `id_kelas` int(11) NOT NULL,
  `kelas` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `kursi`
--

DROP TABLE IF EXISTS `kursi`;
CREATE TABLE `kursi` (
  `id_po` int(11) NOT NULL,
  `kelas` varchar(32) NOT NULL,
  `kolom` varchar(1) NOT NULL,
  `baris` int(11) NOT NULL,
  `no_kursi` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kursi`
--

INSERT INTO `kursi` (`id_po`, `kelas`, `kolom`, `baris`, `no_kursi`) VALUES
(665548, '', 'A', 1, 'A1'),
(665548, '', 'B', 1, 'B1'),
(665548, '', 'C', 1, 'C1'),
(665548, '', 'D', 1, 'D1'),
(665548, '', 'A', 2, 'A2'),
(665548, '', 'B', 2, 'B2'),
(665548, '', 'C', 2, 'C2'),
(665548, '', 'D', 2, 'D2'),
(665548, '', 'A', 3, 'A3'),
(665548, '', 'B', 3, 'B3'),
(665548, '', 'C', 3, 'C3'),
(665548, '', 'D', 3, 'D3'),
(665548, '', 'A', 4, 'A4'),
(665548, '', 'B', 4, 'B4'),
(665548, '', 'C', 4, 'C4'),
(665548, '', 'D', 4, 'D4'),
(665548, '', 'A', 5, 'A5'),
(665548, '', 'B', 5, 'B5'),
(665548, '', 'C', 5, 'C5'),
(665548, '', 'D', 5, 'D5'),
(665548, '', 'A', 6, 'A6'),
(665548, '', 'B', 6, 'B6'),
(665548, '', 'C', 6, 'C6'),
(665548, '', 'D', 6, 'D6'),
(665548, '', 'A', 7, 'A7'),
(665548, '', 'B', 7, 'B7'),
(665548, '', 'C', 7, 'C7'),
(665548, '', 'D', 7, 'D7'),
(665548, '', 'A', 8, 'A8'),
(665548, '', 'B', 8, 'B8'),
(665548, '', 'C', 8, 'C8'),
(665548, '', 'D', 8, 'D8'),
(665548, '', 'A', 9, 'A9'),
(665548, '', 'B', 9, 'B9'),
(665548, '', 'C', 9, 'C9'),
(665548, '', 'D', 9, 'D9'),
(54524, '', 'A', 1, 'A1'),
(54524, '', 'B', 1, 'B1'),
(54524, '', 'A', 2, 'A2'),
(54524, '', 'B', 2, 'B2'),
(54524, '', 'A', 3, 'A3'),
(54524, '', 'B', 3, 'B3'),
(54524, '', 'A', 4, 'A4'),
(54524, '', 'B', 4, 'B4'),
(54524, '', 'A', 5, 'A5'),
(54524, '', 'B', 5, 'B5'),
(54524, '', 'A', 6, 'A6'),
(54524, '', 'B', 6, 'B6'),
(54524, '', 'A', 7, 'A7'),
(54524, '', 'B', 7, 'B7'),
(352720, '', 'A', 1, 'A1'),
(352720, '', 'B', 1, 'B1'),
(352720, '', 'C', 1, 'C1'),
(352720, '', 'D', 1, 'D1'),
(352720, '', 'A', 2, 'A2'),
(352720, '', 'B', 2, 'B2'),
(352720, '', 'C', 2, 'C2'),
(352720, '', 'D', 2, 'D2'),
(352720, '', 'A', 3, 'A3'),
(352720, '', 'B', 3, 'B3'),
(352720, '', 'C', 3, 'C3'),
(352720, '', 'D', 3, 'D3'),
(70491, '', 'A', 1, 'A1'),
(70491, '', 'B', 1, 'B1'),
(70491, '', 'A', 2, 'A2'),
(70491, '', 'B', 2, 'B2'),
(70491, '', 'A', 3, 'A3'),
(70491, '', 'B', 3, 'B3'),
(70491, '', 'A', 4, 'A4'),
(70491, '', 'B', 4, 'B4'),
(70491, '', 'A', 5, 'A5'),
(70491, '', 'B', 5, 'B5'),
(70491, '', 'A', 6, 'A6'),
(70491, '', 'B', 6, 'B6'),
(542491, '', 'A', 1, 'A1'),
(542491, '', 'B', 1, 'B1'),
(542491, '', 'A', 2, 'A2'),
(542491, '', 'B', 2, 'B2'),
(542491, '', 'A', 3, 'A3'),
(542491, '', 'B', 3, 'B3'),
(240968, '', 'A', 1, 'A1'),
(240968, '', 'B', 1, 'B1'),
(240968, '', 'C', 1, 'C1'),
(240968, '', 'D', 1, 'D1'),
(240968, '', 'A', 2, 'A2'),
(240968, '', 'B', 2, 'B2'),
(240968, '', 'C', 2, 'C2'),
(240968, '', 'D', 2, 'D2'),
(240968, '', 'A', 3, 'A3'),
(240968, '', 'B', 3, 'B3'),
(240968, '', 'C', 3, 'C3'),
(240968, '', 'D', 3, 'D3'),
(240968, '', 'A', 4, 'A4'),
(240968, '', 'B', 4, 'B4'),
(240968, '', 'C', 4, 'C4'),
(240968, '', 'D', 4, 'D4'),
(240968, '', 'A', 5, 'A5'),
(240968, '', 'B', 5, 'B5'),
(240968, '', 'C', 5, 'C5'),
(240968, '', 'D', 5, 'D5'),
(240968, '', 'A', 6, 'A6'),
(240968, '', 'B', 6, 'B6'),
(240968, '', 'C', 6, 'C6'),
(240968, '', 'D', 6, 'D6');

-- --------------------------------------------------------

--
-- Table structure for table `pesanan`
--

DROP TABLE IF EXISTS `pesanan`;
CREATE TABLE `pesanan` (
  `id_pesanan` int(12) NOT NULL,
  `id_tiket` int(32) NOT NULL,
  `nama_pemesan` varchar(30) NOT NULL,
  `makanan` varchar(30) NOT NULL,
  `jumlah` int(6) NOT NULL,
  `tagihan` int(16) NOT NULL,
  `status` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pesanan`
--

INSERT INTO `pesanan` (`id_pesanan`, `id_tiket`, `nama_pemesan`, `makanan`, `jumlah`, `tagihan`, `status`) VALUES
(81, 123, 'uuu', 'burger', 1, 20000, 'paid'),
(83, 123, 'aaa', 'spageti', 2, 40000, 'unpaid'),
(97, 432, 'Hanafi', 'spageti', 2, 40000, 'paid'),
(106, 123, 'aa', 'hotdog', 2, 40000, 'unpaid'),
(115, 12033, 'hariawan', 'spageti', 2, 40000, 'paid'),
(128, 20000, '12000', 'hotdog', 12000, 240000000, 'unpaid'),
(141, 1234, 'haryanto', 'spageti', 2, 40000, 'paid');

-- --------------------------------------------------------

--
-- Table structure for table `po`
--

DROP TABLE IF EXISTS `po`;
CREATE TABLE `po` (
  `id_po` int(11) NOT NULL,
  `nama_po` varchar(255) DEFAULT NULL,
  `kelas` varchar(50) DEFAULT NULL,
  `tujuan` varchar(64) NOT NULL,
  `jumlah_kursi` int(11) DEFAULT NULL,
  `harga` int(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `po`
--

INSERT INTO `po` (`id_po`, `nama_po`, `kelas`, `tujuan`, `jumlah_kursi`, `harga`) VALUES
(54524, 'Haryadi', 'Eksekutif', 'Karangmalang', 13, 230000),
(70491, 'Haryanto', 'Eksekutif', 'Wonosobo', 12, 160000),
(240968, 'Bus1', 'Ekonomi', 'Purbalingga', 23, 120000),
(352720, 'Haryanto', 'Ekonomi', 'Wonosobo', 12, 120000),
(542491, 'harry', 'Eksekutif', 'Jakarta', 8, 1500000),
(665548, 'Haryanto', 'Ekonomi', 'Karangklesem', 34, 120000);

--
-- Triggers `po`
--
DROP TRIGGER IF EXISTS `delete_from_kursi_trigger`;
DELIMITER $$
CREATE TRIGGER `delete_from_kursi_trigger` AFTER DELETE ON `po` FOR EACH ROW BEGIN
    DELETE FROM Kursi WHERE id_po = OLD.id_po;
END
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `insert_into_kursi_trigger`;
DELIMITER $$
CREATE TRIGGER `insert_into_kursi_trigger` AFTER INSERT ON `po` FOR EACH ROW BEGIN
    DECLARE jumlah_kursi INT;
    DECLARE jumlah_baris INT;
    DECLARE jumlah_kolom INT;

    -- Ambil nilai jumlah kursi dan kelas dari data yang baru dimasukkan
    SELECT NEW.jumlah_kursi, NEW.kelas INTO jumlah_kursi, @kelas;

    -- Hitung jumlah baris berdasarkan hasil pembagian jumlah kursi dengan jumlah kolom
    SET jumlah_baris = CEIL(jumlah_kursi / (CASE WHEN @kelas = 'Ekonomi' THEN 4 ELSE 2 END));

    -- Atur jumlah kolom berdasarkan jenis kelas (Ekonomi/Eksekutif)
    SET jumlah_kolom = (CASE WHEN @kelas = 'Ekonomi' THEN 4 ELSE 2 END);

    -- Insert ke tabel kursi sesuai dengan ketentuan yang telah diatur
    INSERT INTO Kursi (id_po, baris, kolom, no_kursi)
    SELECT NEW.id_po, 
           (FLOOR((numbers.n - 1) / jumlah_kolom)) + 1 AS baris,
           CASE
                WHEN @kelas = 'Ekonomi' THEN
                    CASE (numbers.n - 1) % 4
                        WHEN 0 THEN 'A'
                        WHEN 1 THEN 'B'
                        WHEN 2 THEN 'C'
                        WHEN 3 THEN 'D'
                    END
                WHEN @kelas = 'Eksekutif' THEN
                    CASE (numbers.n - 1) % 2
                        WHEN 0 THEN 'A'
                        WHEN 1 THEN 'B'
                    END
            END AS kolom,
            CONCAT(
                CASE
                    WHEN @kelas = 'Ekonomi' THEN
                        CASE (numbers.n - 1) % 4
                            WHEN 0 THEN 'A'
                            WHEN 1 THEN 'B'
                            WHEN 2 THEN 'C'
                            WHEN 3 THEN 'D'
                        END
                    WHEN @kelas = 'Eksekutif' THEN
                        CASE (numbers.n - 1) % 2
                            WHEN 0 THEN 'A'
                            WHEN 1 THEN 'B'
                        END
                END,
                (FLOOR((numbers.n - 1) / jumlah_kolom)) + 1
            ) AS no_kursi
    FROM (
        SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n 
        FROM information_schema.tables
    ) AS numbers
    WHERE numbers.n <= jumlah_baris * jumlah_kolom;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `tiketterbeli`
--

DROP TABLE IF EXISTS `tiketterbeli`;
CREATE TABLE `tiketterbeli` (
  `id_tiket` int(11) NOT NULL,
  `id_keberangkatan` int(12) NOT NULL,
  `namaPenumpang` varchar(255) DEFAULT NULL,
  `tujuan` varchar(255) DEFAULT NULL,
  `tanggal_keberangkatan` date DEFAULT NULL,
  `po` varchar(64) DEFAULT NULL,
  `noKursi` varchar(11) DEFAULT NULL,
  `kelas` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tiketterbeli`
--

INSERT INTO `tiketterbeli` (`id_tiket`, `id_keberangkatan`, `namaPenumpang`, `tujuan`, `tanggal_keberangkatan`, `po`, `noKursi`, `kelas`) VALUES
(1207167, 18151, 'haryanto', 'Purbalingga', '0000-00-00', 'Haryanto', 'B2', 'Ekonomi'),
(6415347, 18151, 'aa', 'Purbalingga', '0000-00-00', 'Haryanto', 'A2', 'Ekonomi'),
(6441922, 110978, 'sule', 'Karangmalang', '2023-12-12', 'Haryadi', 'B1', 'Eksekutif');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `harga`
--
ALTER TABLE `harga`
  ADD PRIMARY KEY (`id_harga`),
  ADD KEY `fk_harga_po` (`id_po`),
  ADD KEY `fk_harga_kelas` (`kelas_id`);

--
-- Indexes for table `keberangkatan`
--
ALTER TABLE `keberangkatan`
  ADD PRIMARY KEY (`id_keberangkatan`),
  ADD KEY `fk_keberangkatan_po` (`id_po`);

--
-- Indexes for table `kelas`
--
ALTER TABLE `kelas`
  ADD PRIMARY KEY (`id_kelas`);

--
-- Indexes for table `kursi`
--
ALTER TABLE `kursi`
  ADD KEY `id_po` (`id_po`);

--
-- Indexes for table `pesanan`
--
ALTER TABLE `pesanan`
  ADD PRIMARY KEY (`id_pesanan`);

--
-- Indexes for table `po`
--
ALTER TABLE `po`
  ADD PRIMARY KEY (`id_po`);

--
-- Indexes for table `tiketterbeli`
--
ALTER TABLE `tiketterbeli`
  ADD PRIMARY KEY (`id_tiket`),
  ADD KEY `fk_tiket_po` (`po`),
  ADD KEY `id_keberangkatan` (`id_keberangkatan`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `harga`
--
ALTER TABLE `harga`
  MODIFY `id_harga` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `keberangkatan`
--
ALTER TABLE `keberangkatan`
  MODIFY `id_keberangkatan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=667311;

--
-- AUTO_INCREMENT for table `kelas`
--
ALTER TABLE `kelas`
  MODIFY `id_kelas` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `po`
--
ALTER TABLE `po`
  MODIFY `id_po` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2032019612;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `harga`
--
ALTER TABLE `harga`
  ADD CONSTRAINT `fk_harga_kelas` FOREIGN KEY (`kelas_id`) REFERENCES `kelas` (`id_kelas`);

--
-- Constraints for table `keberangkatan`
--
ALTER TABLE `keberangkatan`
  ADD CONSTRAINT `fk_keberangkatan_po` FOREIGN KEY (`id_po`) REFERENCES `po` (`id_po`);

--
-- Constraints for table `tiketterbeli`
--
ALTER TABLE `tiketterbeli`
  ADD CONSTRAINT `tiketterbeli_ibfk_1` FOREIGN KEY (`id_keberangkatan`) REFERENCES `keberangkatan` (`id_keberangkatan`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
