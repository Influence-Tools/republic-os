---
type: Jurisdiction
title: "Morton County, ND"
classification: county
fips: "38059"
state: "ND"
demographics:
  population: 33777
  population_under_18: 7723
  population_18_64: 20207
  population_65_plus: 5847
  median_household_income: 79382
  poverty_rate: 8.04
  homeownership_rate: 74.15
  unemployment_rate: 1.53
  median_home_value: 263900
  gini_index: 0.4626
  vacancy_rate: 9.82
  race_white: 29426
  race_black: 548
  race_asian: 46
  race_native: 1376
  hispanic: 1486
  bachelors_plus: 8223
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/31"
    rel: in-district
    area_weight: 0.4907
  - to: "us/states/nd/districts/senate/36"
    rel: in-district
    area_weight: 0.4272
  - to: "us/states/nd/districts/senate/33"
    rel: in-district
    area_weight: 0.0766
  - to: "us/states/nd/districts/senate/34"
    rel: in-district
    area_weight: 0.0055
  - to: "us/states/nd/districts/house/31"
    rel: in-district
    area_weight: 0.4907
  - to: "us/states/nd/districts/house/36"
    rel: in-district
    area_weight: 0.4272
  - to: "us/states/nd/districts/house/33"
    rel: in-district
    area_weight: 0.0766
  - to: "us/states/nd/districts/house/34"
    rel: in-district
    area_weight: 0.0055
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Morton County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33777 |
| Under 18 | 7723 |
| 18–64 | 20207 |
| 65+ | 5847 |
| Median household income | 79382 |
| Poverty rate | 8.04 |
| Homeownership rate | 74.15 |
| Unemployment rate | 1.53 |
| Median home value | 263900 |
| Gini index | 0.4626 |
| Vacancy rate | 9.82 |
| White | 29426 |
| Black | 548 |
| Asian | 46 |
| Native | 1376 |
| Hispanic/Latino | 1486 |
| Bachelor's or higher | 8223 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 31](/us/states/nd/districts/senate/31.md) — 49% (state senate)
- [ND Senate District 36](/us/states/nd/districts/senate/36.md) — 43% (state senate)
- [ND Senate District 33](/us/states/nd/districts/senate/33.md) — 8% (state senate)
- [ND Senate District 34](/us/states/nd/districts/senate/34.md) — 1% (state senate)
- [ND House District 31](/us/states/nd/districts/house/31.md) — 49% (state house)
- [ND House District 36](/us/states/nd/districts/house/36.md) — 43% (state house)
- [ND House District 33](/us/states/nd/districts/house/33.md) — 8% (state house)
- [ND House District 34](/us/states/nd/districts/house/34.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
