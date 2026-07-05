---
type: Jurisdiction
title: "Howard County, MD"
classification: county
fips: "24027"
state: "MD"
demographics:
  population: 336328
  population_under_18: 79917
  population_18_64: 205136
  population_65_plus: 51275
  median_household_income: 149763
  poverty_rate: 5.23
  homeownership_rate: 71.48
  unemployment_rate: 3.49
  median_home_value: 597900
  gini_index: 0.4136
  vacancy_rate: 3.37
  race_white: 157552
  race_black: 67150
  race_asian: 64745
  race_native: 1091
  hispanic: 29135
  bachelors_plus: 226665
districts:
  - to: "us/states/md/districts/03"
    rel: in-district
    area_weight: 0.9939
  - to: "us/states/md/districts/senate/9"
    rel: in-district
    area_weight: 0.6204
  - to: "us/states/md/districts/senate/13"
    rel: in-district
    area_weight: 0.2691
  - to: "us/states/md/districts/senate/12"
    rel: in-district
    area_weight: 0.1096
  - to: "us/states/md/districts/house/9a"
    rel: in-district
    area_weight: 0.5414
  - to: "us/states/md/districts/house/13"
    rel: in-district
    area_weight: 0.2691
  - to: "us/states/md/districts/house/12a"
    rel: in-district
    area_weight: 0.1096
  - to: "us/states/md/districts/house/9b"
    rel: in-district
    area_weight: 0.0789
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# Howard County, MD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 336328 |
| Under 18 | 79917 |
| 18–64 | 205136 |
| 65+ | 51275 |
| Median household income | 149763 |
| Poverty rate | 5.23 |
| Homeownership rate | 71.48 |
| Unemployment rate | 3.49 |
| Median home value | 597900 |
| Gini index | 0.4136 |
| Vacancy rate | 3.37 |
| White | 157552 |
| Black | 67150 |
| Asian | 64745 |
| Native | 1091 |
| Hispanic/Latino | 29135 |
| Bachelor's or higher | 226665 |

## Districts

- [MD-03](/us/states/md/districts/03.md) — 99% (congressional)
- [MD Senate District 9](/us/states/md/districts/senate/9.md) — 62% (state senate)
- [MD Senate District 13](/us/states/md/districts/senate/13.md) — 27% (state senate)
- [MD Senate District 12](/us/states/md/districts/senate/12.md) — 11% (state senate)
- [MD House District 9A](/us/states/md/districts/house/9a.md) — 54% (state house)
- [MD House District 13](/us/states/md/districts/house/13.md) — 27% (state house)
- [MD House District 12A](/us/states/md/districts/house/12a.md) — 11% (state house)
- [MD House District 9B](/us/states/md/districts/house/9b.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
