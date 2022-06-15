-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 09, 2022 at 09:07 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `certificate_locker`
--

-- --------------------------------------------------------

--
-- Table structure for table `nt_blockchain`
--

CREATE TABLE `nt_blockchain` (
  `id` int(11) NOT NULL default '0',
  `block_id` int(11) NOT NULL,
  `pre_hash` varchar(200) NOT NULL,
  `hash_value` varchar(200) NOT NULL,
  `sdata` varchar(200) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `nt_blockchain`
--

INSERT INTO `nt_blockchain` (`id`, `block_id`, `pre_hash`, `hash_value`, `sdata`) VALUES
(1, 1, '00000000000000000000000000000000', 'a6ac94b0bac1e2c747ee95628d6dc78e', 'ID:1,User:Sathish, CAN No.:CN01221, Key:e3663750, RegDate:12-01-2022'),
(7, 1, 'eeb314660de63a388e5d4b1f394a7156', 'e7902b89edc66584e1cdf4d8ab31ef8e', 'ID:1,User:Dinesh, KYC Code:CN05221, Key:615ba30a, RegDate:22-05-2022'),
(8, 2, 'e7902b89edc66584e1cdf4d8ab31ef8e', '0ddc05abae1af1f6e6c2659386b24bf5', 'ID:2,User:Dinesh, KYC Code:CN05222, Key:7683df02, RegDate:22-05-2022'),
(9, 1, '0ddc05abae1af1f6e6c2659386b24bf5', '380289db99e77033b81f7e5b48051d06', 'ID:1,User:Dinesh, KYC Code:CN05221, Key:cb0ed4a6, RegDate:22-05-2022'),
(10, 2, '380289db99e77033b81f7e5b48051d06', '8ec3847490c8ec3d1a3ca0107c4ed7a1', 'ID:2,User:Dinesh, KYC Code:CN05222, Key:a0675f17, RegDate:22-05-2022'),
(11, 1, '8ec3847490c8ec3d1a3ca0107c4ed7a1', '368c68bbac9a5d56aeaf0ec7d168ef80', 'ID:1,User:Dinesh, KYC Code:CN05221, RegDate:22-05-2022, Access by dinesh'),
(12, 1, '368c68bbac9a5d56aeaf0ec7d168ef80', '368c68bbac9a5d56aeaf0ec7d168ef80', 'ID:1,User:Dinesh, KYC Code:CN05221, RegDate:22-05-2022, Access by dinesh'),
(13, 3, '368c68bbac9a5d56aeaf0ec7d168ef80', '6b5553262fb42f6f3950581950616104', 'ID:3,User:Dinesh, KYC Code:CN05223, Key:36b8f3e2, RegDate:22-05-2022'),
(14, 1, '6b5553262fb42f6f3950581950616104', '368c68bbac9a5d56aeaf0ec7d168ef80', 'ID:1,User:Dinesh, KYC Code:CN05221, RegDate:22-05-2022, Access by dinesh'),
(15, 4, '368c68bbac9a5d56aeaf0ec7d168ef80', '5d0da0a58c614aad84589797afb70d08', 'ID:4,User:Dinesh, KYC Code:CN06224, Key:6f80dab1, RegDate:01-06-2022'),
(16, 2, '5d0da0a58c614aad84589797afb70d08', 'fe16dd13d7af5c0da9d3dffb2e5a80e3', 'ID:2,User:Dinesh, KYC Code:CN05222, RegDate:01-06-2022, Access by dinesh'),
(17, 5, 'fe16dd13d7af5c0da9d3dffb2e5a80e3', '75db83d4b35fb68ad5be84d880a820bd', 'ID:5,User:Raju, KYC Code:CN06225, Key:63db80aa, RegDate:09-06-2022'),
(18, 6, '75db83d4b35fb68ad5be84d880a820bd', 'd4005a68bb8affbf18755fec0981b364', 'ID:6,User:Raju, KYC Code:CN06226, Key:3c8d9169, RegDate:09-06-2022'),
(19, 1, 'd4005a68bb8affbf18755fec0981b364', '97b731516440ef38b48658189552e16b', 'ID:1,User:Sathish, KYC Code:CN06221, Key:42e0da24, RegDate:10-06-2022'),
(20, 1, '97b731516440ef38b48658189552e16b', '57580bc5342a97abf193228afdf6416d', 'ID:1,User:Sathish, KYC Code:CN06221, RegDate:10-06-2022, Access by unauthorized'),
(21, 1, '57580bc5342a97abf193228afdf6416d', '358ed719c72d6e16be1e80d4b009571a', 'ID:1,User:Sathish, KYC Code:CN06221, RegDate:10-06-2022'),
(22, 1, '358ed719c72d6e16be1e80d4b009571a', '358ed719c72d6e16be1e80d4b009571a', 'ID:1,User:Sathish, KYC Code:CN06221, RegDate:10-06-2022'),
(23, 1, '358ed719c72d6e16be1e80d4b009571a', '358ed719c72d6e16be1e80d4b009571a', 'ID:1,User:Sathish, KYC Code:CN06221, RegDate:10-06-2022'),
(24, 1, '358ed719c72d6e16be1e80d4b009571a', '57580bc5342a97abf193228afdf6416d', 'ID:1,User:Sathish, KYC Code:CN06221, RegDate:10-06-2022, Access by unauthorized'),
(25, 1, '57580bc5342a97abf193228afdf6416d', 'd5ff1857f8b2f8ca9a2c72542e213ce5', 'ID:1,User:Sathish, KYC Code:CN06221, RegDate:10-06-2022, Access by sathish');

-- --------------------------------------------------------

--
-- Table structure for table `nt_cca`
--

CREATE TABLE `nt_cca` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `address` varchar(40) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `utype` varchar(20) NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `nt_cca`
--

INSERT INTO `nt_cca` (`id`, `name`, `mobile`, `email`, `address`, `uname`, `pass`, `state`, `utype`, `status`) VALUES
(1, 'Rajiv', 9034566264, 'cca_verify@gmail.com', 'Chennai', 'CCA1', '12345', '', 'CCA', 1),
(3, 'Rama', 9894918800, 'rndittrichy@gmail.com', '33,ss', 'rama', '1234', '', '', 1);

-- --------------------------------------------------------

--
-- Table structure for table `nt_certificate`
--

CREATE TABLE `nt_certificate` (
  `id` int(11) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `ctype` varchar(30) NOT NULL,
  `filename` varchar(50) NOT NULL,
  `detail` varchar(100) NOT NULL,
  `rdate` varchar(20) NOT NULL,
  `status` int(11) NOT NULL,
  `canno` varchar(20) NOT NULL,
  `transfer_sii` varchar(20) NOT NULL,
  `transfer_siv` varchar(20) NOT NULL,
  `transfer_ccv` varchar(20) NOT NULL,
  `transfer_cca` varchar(20) NOT NULL,
  `ckey` varchar(20) NOT NULL,
  `c_status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `nt_certificate`
--

INSERT INTO `nt_certificate` (`id`, `uname`, `ctype`, `filename`, `detail`, `rdate`, `status`, `canno`, `transfer_sii`, `transfer_siv`, `transfer_ccv`, `transfer_cca`, `ckey`, `c_status`) VALUES
(1, 'sathish', '', 'F1birth4.png', 'degree certificate', '10-06-2022', 1, 'CN06221', '', '', '', '', '42e0da24', 1);

-- --------------------------------------------------------

--
-- Table structure for table `nt_login`
--

CREATE TABLE `nt_login` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `nt_login`
--

INSERT INTO `nt_login` (`username`, `password`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `nt_proof`
--

CREATE TABLE `nt_proof` (
  `id` int(11) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `cid` int(11) NOT NULL,
  `filename` varchar(50) NOT NULL,
  `detail` varchar(100) NOT NULL,
  `rdate` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `nt_proof`
--


-- --------------------------------------------------------

--
-- Table structure for table `nt_register`
--

CREATE TABLE `nt_register` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `address` varchar(50) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL,
  `private_key` varchar(20) NOT NULL,
  `public_key` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `nt_register`
--

INSERT INTO `nt_register` (`id`, `name`, `mobile`, `email`, `address`, `uname`, `pass`, `private_key`, `public_key`) VALUES
(1, 'Sathish', 9988776655, 'sathish@gmail.com', '433/3,GS Road, Namakkal', 'sathish', '1234', '078dc595', 'e3663750');

-- --------------------------------------------------------

--
-- Table structure for table `nt_require`
--

CREATE TABLE `nt_require` (
  `id` int(11) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `cid` int(11) NOT NULL,
  `detail` varchar(100) NOT NULL,
  `rdate` varchar(20) NOT NULL,
  `verifier` varchar(20) NOT NULL,
  `cno` varchar(20) NOT NULL,
  `ckey` varchar(20) NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `nt_require`
--

INSERT INTO `nt_require` (`id`, `uname`, `cid`, `detail`, `rdate`, `verifier`, `cno`, `ckey`, `status`) VALUES
(1, 'sathish', 1, 'degree certificate', '10-06-2022', 'rama', 'CN06221', 'e3663750', 1);
