-- Estructura de tabla para la tabla `procedures`
--

CREATE TABLE procedures (
  id bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  date date NOT NULL,
  description text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  procedure_type_id bigint(20) UNSIGNED NOT NULL,
  tree_id bigint(20) UNSIGNED NOT NULL,
  responsible_id bigint(20) UNSIGNED NOT NULL,
  user_id bigint(20) UNSIGNED NOT NULL,
  created_at timestamp NULL DEFAULT NULL,
  updated_at timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- CREATE TABLE juegos(
--     id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     nombre VARCHAR(255) NOT NULL,
--     descripcion VARCHAR(255) NOT NULL,
--     precio DECIMAL(9,2) NOT NULL
-- );

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `procedure_types`
--

CREATE TABLE procedure_types (
  id bigint(20) UNSIGNED NOT NULLAUTO_INCREMENT PRIMARY KEY,
  name varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  description text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  created_at timestamp NULL DEFAULT NULL,
  updated_at timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `procedure_types`
--

INSERT INTO `procedure_types` (`id`, `name`, `description`, `created_at`, `updated_at`) VALUES
(1, 'Sembrado', NULL, '2022-05-23 21:21:02', '2022-05-23 21:21:02'),
(2, 'Abonado', NULL, '2022-05-23 21:21:15', '2022-05-23 21:21:15'),
(3, 'Control de plagas', NULL, '2022-05-23 21:21:29', '2022-05-23 21:21:29'),
(4, 'Deshiervo', NULL, '2022-05-23 21:21:40', '2022-05-23 21:23:57'),
(5, 'Incidencias', NULL, '2022-05-23 21:23:38', '2022-05-23 21:23:38'),
(6, 'Regado', NULL, '2022-05-23 22:15:22', '2022-05-23 22:15:22');