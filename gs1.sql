-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 29, 2019 at 08:23 AM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gs1`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts_employee`
--

CREATE TABLE `accounts_employee` (
  `id` int(11) NOT NULL,
  `address` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone` varchar(14) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_of_birth` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `next_of_kin_name` varchar(60) COLLATE utf8mb4_unicode_ci NOT NULL,
  `kin_email` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `county` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `next_of_kin_phone` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dependant_name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dependant_relationship` varchar(60) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dependant_contact` varchar(60) COLLATE utf8mb4_unicode_ci NOT NULL,
  `salary` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `department_id` int(11) NOT NULL,
  `position_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `alt_phone_number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `accounts_employee`
--

INSERT INTO `accounts_employee` (`id`, `address`, `phone`, `date_of_birth`, `next_of_kin_name`, `kin_email`, `county`, `next_of_kin_phone`, `dependant_name`, `dependant_relationship`, `dependant_contact`, `salary`, `department_id`, `position_id`, `user_id`, `alt_phone_number`) VALUES
(1, 'Kisumu-K', '07051545121', '2019-01-16', '', 'junior@gmail.com', '', '', 'Omambia Daug', 'Son', '074404509', '20000', 1, 1, 1, 751545121);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add employee', 7, 'add_employee'),
(26, 'Can change employee', 7, 'change_employee'),
(27, 'Can delete employee', 7, 'delete_employee'),
(28, 'Can view employee', 7, 'view_employee'),
(29, 'Can add apply leave', 8, 'add_applyleave'),
(30, 'Can change apply leave', 8, 'change_applyleave'),
(31, 'Can delete apply leave', 8, 'delete_applyleave'),
(32, 'Can view apply leave', 8, 'view_applyleave'),
(33, 'Can add leave', 9, 'add_leave'),
(34, 'Can change leave', 9, 'change_leave'),
(35, 'Can delete leave', 9, 'delete_leave'),
(36, 'Can view leave', 9, 'view_leave'),
(37, 'Can add department', 10, 'add_department'),
(38, 'Can change department', 10, 'change_department'),
(39, 'Can delete department', 10, 'delete_department'),
(40, 'Can view department', 10, 'view_department'),
(41, 'Can add position', 11, 'add_position'),
(42, 'Can change position', 11, 'change_position'),
(43, 'Can delete position', 11, 'delete_position'),
(44, 'Can view position', 11, 'view_position'),
(45, 'Can add target', 12, 'add_target'),
(46, 'Can change target', 12, 'change_target'),
(47, 'Can delete target', 12, 'delete_target'),
(48, 'Can view target', 12, 'view_target'),
(49, 'Can add client', 13, 'add_client'),
(50, 'Can change client', 13, 'change_client'),
(51, 'Can delete client', 13, 'delete_client'),
(52, 'Can view client', 13, 'view_client'),
(53, 'Can add feedback', 14, 'add_feedback'),
(54, 'Can change feedback', 14, 'change_feedback'),
(55, 'Can delete feedback', 14, 'delete_feedback'),
(56, 'Can view feedback', 14, 'view_feedback'),
(57, 'Can add supplier', 15, 'add_supplier'),
(58, 'Can change supplier', 15, 'change_supplier'),
(59, 'Can delete supplier', 15, 'delete_supplier'),
(60, 'Can view supplier', 15, 'view_supplier'),
(61, 'Can add training', 16, 'add_training'),
(62, 'Can change training', 16, 'change_training'),
(63, 'Can delete training', 16, 'delete_training'),
(64, 'Can view training', 16, 'view_training');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'argon2$argon2i$v=19$m=512,t=2,p=2$ekZJcGRjeWxscEZZ$o8sU42ChUu8MUMSRLkP19Q', '2019-01-28 18:00:04.189952', 0, 'omambia', 'Omambia', 'Dauglous', 'omambiadauglous@gmail.com', 0, 1, '2019-01-28 17:59:33.409242');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `CRM_client`
--

CREATE TABLE `CRM_client` (
  `id` int(11) NOT NULL,
  `company_name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `company_phone` int(11) NOT NULL,
  `company_phone_alt` int(11) NOT NULL,
  `company_email` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `company_email_alt` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `post_address` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `physical_location` varchar(60) COLLATE utf8mb4_unicode_ci NOT NULL,
  `director_info` varchar(1000) COLLATE utf8mb4_unicode_ci NOT NULL,
  `sector` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `category` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_of_issue` date NOT NULL,
  `nature_of_business` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `certificate_of_incorporation` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `copy_of_id` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `copy_of_blank_cheque` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `copy_of_trade_licence` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `list_of_product_barcoded` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `director_pin_number` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `company_certificate_pin` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `copy_of_kebs_certicate` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `CRM_client`
--

INSERT INTO `CRM_client` (`id`, `company_name`, `company_phone`, `company_phone_alt`, `company_email`, `company_email_alt`, `post_address`, `physical_location`, `director_info`, `sector`, `category`, `date_of_issue`, `nature_of_business`, `certificate_of_incorporation`, `copy_of_id`, `copy_of_blank_cheque`, `copy_of_trade_licence`, `list_of_product_barcoded`, `director_pin_number`, `company_certificate_pin`, `copy_of_kebs_certicate`) VALUES
(1, 'BrugKe', 701246475, 701246475, 'kafomombia@gmail.com', 'kafomambia@gmial.com', '01004', 'Nairobi', 'GS1Kenya. 07050424525', 'HELATHCARE', 'CATEGORY B', '2019-01-16', 'Large', 'documents/clients/ef5a3c4f6348421c8e37afd32dc04fc7.pdf', 'documents/clients/29c47c7760ba483eab11f417296c0716.pdf', 'documents/clients/89426bfc37af4b9a97252767b913af86.pdf', 'documents/clients/faa1a83216d9480b9b8bbaee9476f20e.pdf', 'documents/clients/03de7a21ec994665bfc19d737867188f.pdf', 'documents/clients/0967531a25464e3e805282a150988d46.pdf', 'documents/clients/ef561cd4d42343378af77ca19422e153.pdf', 'documents/clients/0bb35ead1b744cc2b40e72a04996109b.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `CRM_feedback`
--

CREATE TABLE `CRM_feedback` (
  `id` int(11) NOT NULL,
  `feedback` varchar(1000) COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` tinyint(1) NOT NULL,
  `client_name_id` int(11) NOT NULL,
  `created_on` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `CRM_feedback`
--

INSERT INTO `CRM_feedback` (`id`, `feedback`, `status`, `client_name_id`, `created_on`) VALUES
(1, 'Very honest work', 0, 1, '2019-01-29');

-- --------------------------------------------------------

--
-- Table structure for table `CRM_supplier`
--

CREATE TABLE `CRM_supplier` (
  `id` int(11) NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone` int(11) NOT NULL,
  `country` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `website` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` varchar(1000) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `CRM_supplier`
--

INSERT INTO `CRM_supplier` (`id`, `name`, `phone`, `country`, `website`, `description`) VALUES
(1, 'Kem Keni', 701246475, 'Kenya', 'http:123456677.com', 'Some extra');

-- --------------------------------------------------------

--
-- Table structure for table `CRM_training`
--

CREATE TABLE `CRM_training` (
  `id` int(11) NOT NULL,
  `trainer_id` int(11) NOT NULL,
  `happened_on` date NOT NULL,
  `number_of_trainee` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `CRM_training`
--

INSERT INTO `CRM_training` (`id`, `trainer_id`, `happened_on`, `number_of_trainee`) VALUES
(1, 1, '2019-01-29', 14);

-- --------------------------------------------------------

--
-- Table structure for table `departments_department`
--

CREATE TABLE `departments_department` (
  `id` int(11) NOT NULL,
  `name` varchar(256) COLLATE utf8mb4_unicode_ci NOT NULL,
  `initials` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_on` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `departments_department`
--

INSERT INTO `departments_department` (`id`, `name`, `initials`, `created_on`) VALUES
(1, 'Human Resource', 'HR', '2019-01-28');

-- --------------------------------------------------------

--
-- Table structure for table `departments_position`
--

CREATE TABLE `departments_position` (
  `id` int(11) NOT NULL,
  `name` varchar(256) COLLATE utf8mb4_unicode_ci NOT NULL,
  `initials` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_on` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `departments_position`
--

INSERT INTO `departments_position` (`id`, `name`, `initials`, `created_on`) VALUES
(1, 'Manager', 'HRM', '2019-01-28');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'accounts', 'employee'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(13, 'CRM', 'client'),
(14, 'CRM', 'feedback'),
(15, 'CRM', 'supplier'),
(16, 'CRM', 'training'),
(10, 'departments', 'department'),
(11, 'departments', 'position'),
(8, 'leave', 'applyleave'),
(9, 'leave', 'leave'),
(6, 'sessions', 'session'),
(12, 'targets', 'target');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'departments', '0001_initial', '2019-01-28 15:43:40.414350'),
(2, 'contenttypes', '0001_initial', '2019-01-28 15:43:40.790622'),
(3, 'auth', '0001_initial', '2019-01-28 15:43:47.214942'),
(4, 'accounts', '0001_initial', '2019-01-28 15:43:50.010549'),
(5, 'accounts', '0002_auto_20190125_0913', '2019-01-28 15:43:50.102518'),
(6, 'CRM', '0001_initial', '2019-01-28 15:43:52.569360'),
(7, 'CRM', '0002_auto_20190125_1030', '2019-01-28 15:43:52.629527'),
(8, 'CRM', '0003_auto_20190125_1049', '2019-01-28 15:43:53.333161'),
(9, 'CRM', '0004_auto_20190125_1052', '2019-01-28 15:43:54.141554'),
(10, 'CRM', '0005_feedback_created_on', '2019-01-28 15:43:54.563921'),
(11, 'CRM', '0006_auto_20190125_1200', '2019-01-28 15:43:55.403908'),
(12, 'CRM', '0007_auto_20190127_1038', '2019-01-28 15:43:56.018315'),
(13, 'accounts', '0003_employee_alt_phone_number', '2019-01-28 15:43:56.485077'),
(14, 'admin', '0001_initial', '2019-01-28 15:43:57.997041'),
(15, 'admin', '0002_logentry_remove_auto_add', '2019-01-28 15:43:58.046333'),
(16, 'admin', '0003_logentry_add_action_flag_choices', '2019-01-28 15:43:58.098744'),
(17, 'contenttypes', '0002_remove_content_type_name', '2019-01-28 15:43:58.860067'),
(18, 'auth', '0002_alter_permission_name_max_length', '2019-01-28 15:43:59.489170'),
(19, 'auth', '0003_alter_user_email_max_length', '2019-01-28 15:44:00.034311'),
(20, 'auth', '0004_alter_user_username_opts', '2019-01-28 15:44:00.080112'),
(21, 'auth', '0005_alter_user_last_login_null', '2019-01-28 15:44:00.487756'),
(22, 'auth', '0006_require_contenttypes_0002', '2019-01-28 15:44:00.564349'),
(23, 'auth', '0007_alter_validators_add_error_messages', '2019-01-28 15:44:00.653732'),
(24, 'auth', '0008_alter_user_username_max_length', '2019-01-28 15:44:01.224207'),
(25, 'auth', '0009_alter_user_last_name_max_length', '2019-01-28 15:44:01.896548'),
(26, 'leave', '0001_initial', '2019-01-28 15:44:05.248096'),
(27, 'sessions', '0001_initial', '2019-01-28 15:44:05.726268'),
(28, 'targets', '0001_initial', '2019-01-28 15:44:06.930275'),
(29, 'targets', '0002_auto_20190114_0749', '2019-01-28 15:44:06.988403'),
(30, 'targets', '0003_auto_20190114_0751', '2019-01-28 15:44:07.036846'),
(31, 'CRM', '0008_remove_training_topic', '2019-01-29 07:20:14.576211'),
(32, 'leave', '0002_auto_20190129_0738', '2019-01-29 07:38:20.797441');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('vqyxl3hpqiar7vudllni1tdt8joyu8ta', 'MjBkZDIyZGQ4OWQ2MjkxNWVkOWU5ODFmYjZkYTgyZjNlODhkODgwZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkZWUxNmIxOWRjOTZiYThlODBjNDdlNmJiZmRjY2EzNmFkYmJkZmVhIiwidXNlcm5hbWUiOiJvbWFtYmlhIn0=', '2019-02-11 18:00:04.248476');

-- --------------------------------------------------------

--
-- Table structure for table `leave_applyleave`
--

CREATE TABLE `leave_applyleave` (
  `id` int(11) NOT NULL,
  `start_date` date NOT NULL,
  `status` int(11) NOT NULL,
  `end_date` date NOT NULL,
  `resume_date` date NOT NULL,
  `home_phone` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `employee_id` int(11) NOT NULL,
  `leave_id` int(11) NOT NULL,
  `person_taking_charge_id` int(11) NOT NULL,
  `period` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `leave_applyleave`
--

INSERT INTO `leave_applyleave` (`id`, `start_date`, `status`, `end_date`, `resume_date`, `home_phone`, `employee_id`, `leave_id`, `person_taking_charge_id`, `period`) VALUES
(1, '2019-01-16', 1, '2019-01-31', '2019-02-01', '0708067459', 1, 1, 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `leave_leave`
--

CREATE TABLE `leave_leave` (
  `id` int(11) NOT NULL,
  `name` varchar(256) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` varchar(256) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_on` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `leave_leave`
--

INSERT INTO `leave_leave` (`id`, `name`, `description`, `created_on`) VALUES
(1, 'Sick Leave', 'Given any employee seeking medical attention', '2019-01-29');

-- --------------------------------------------------------

--
-- Table structure for table `targets_target`
--

CREATE TABLE `targets_target` (
  `id` int(11) NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `status` varchar(70) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_of_appraisal` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `who_appraised` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `employee_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts_employee`
--
ALTER TABLE `accounts_employee`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD KEY `accounts_employee_department_id_28acdfd0_fk_departmen` (`department_id`),
  ADD KEY `accounts_employee_position_id_3f7cd7b7_fk_departmen` (`position_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `CRM_client`
--
ALTER TABLE `CRM_client`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `CRM_feedback`
--
ALTER TABLE `CRM_feedback`
  ADD PRIMARY KEY (`id`),
  ADD KEY `CRM_feedback_client_name_id_062eebbb_fk_CRM_client_id` (`client_name_id`);

--
-- Indexes for table `CRM_supplier`
--
ALTER TABLE `CRM_supplier`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `CRM_training`
--
ALTER TABLE `CRM_training`
  ADD PRIMARY KEY (`id`),
  ADD KEY `CRM_training_trainer_id_9d2300d5_fk_accounts_employee_id` (`trainer_id`);

--
-- Indexes for table `departments_department`
--
ALTER TABLE `departments_department`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `departments_position`
--
ALTER TABLE `departments_position`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `leave_applyleave`
--
ALTER TABLE `leave_applyleave`
  ADD PRIMARY KEY (`id`),
  ADD KEY `leave_applyleave_leave_id_24f45d69_fk_leave_leave_id` (`leave_id`),
  ADD KEY `leave_applyleave_person_taking_charge_ca981a05_fk_accounts_` (`person_taking_charge_id`),
  ADD KEY `leave_applyleave_employee_id_02bd00e1_fk_accounts_employee_id` (`employee_id`);

--
-- Indexes for table `leave_leave`
--
ALTER TABLE `leave_leave`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `targets_target`
--
ALTER TABLE `targets_target`
  ADD PRIMARY KEY (`id`),
  ADD KEY `targets_target_employee_id_18397c0c_fk_accounts_employee_id` (`employee_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts_employee`
--
ALTER TABLE `accounts_employee`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `CRM_client`
--
ALTER TABLE `CRM_client`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `CRM_feedback`
--
ALTER TABLE `CRM_feedback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `CRM_supplier`
--
ALTER TABLE `CRM_supplier`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `CRM_training`
--
ALTER TABLE `CRM_training`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `departments_department`
--
ALTER TABLE `departments_department`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `departments_position`
--
ALTER TABLE `departments_position`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `leave_applyleave`
--
ALTER TABLE `leave_applyleave`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `leave_leave`
--
ALTER TABLE `leave_leave`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `targets_target`
--
ALTER TABLE `targets_target`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accounts_employee`
--
ALTER TABLE `accounts_employee`
  ADD CONSTRAINT `accounts_employee_department_id_28acdfd0_fk_departmen` FOREIGN KEY (`department_id`) REFERENCES `departments_department` (`id`),
  ADD CONSTRAINT `accounts_employee_position_id_3f7cd7b7_fk_departmen` FOREIGN KEY (`position_id`) REFERENCES `departments_position` (`id`),
  ADD CONSTRAINT `accounts_employee_user_id_593173d8_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `CRM_feedback`
--
ALTER TABLE `CRM_feedback`
  ADD CONSTRAINT `CRM_feedback_client_name_id_062eebbb_fk_CRM_client_id` FOREIGN KEY (`client_name_id`) REFERENCES `CRM_client` (`id`);

--
-- Constraints for table `CRM_training`
--
ALTER TABLE `CRM_training`
  ADD CONSTRAINT `CRM_training_trainer_id_9d2300d5_fk_accounts_employee_id` FOREIGN KEY (`trainer_id`) REFERENCES `accounts_employee` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `leave_applyleave`
--
ALTER TABLE `leave_applyleave`
  ADD CONSTRAINT `leave_applyleave_employee_id_02bd00e1_fk_accounts_employee_id` FOREIGN KEY (`employee_id`) REFERENCES `accounts_employee` (`id`),
  ADD CONSTRAINT `leave_applyleave_leave_id_24f45d69_fk_leave_leave_id` FOREIGN KEY (`leave_id`) REFERENCES `leave_leave` (`id`),
  ADD CONSTRAINT `leave_applyleave_person_taking_charge_ca981a05_fk_accounts_` FOREIGN KEY (`person_taking_charge_id`) REFERENCES `accounts_employee` (`id`);

--
-- Constraints for table `targets_target`
--
ALTER TABLE `targets_target`
  ADD CONSTRAINT `targets_target_employee_id_18397c0c_fk_accounts_employee_id` FOREIGN KEY (`employee_id`) REFERENCES `accounts_employee` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
