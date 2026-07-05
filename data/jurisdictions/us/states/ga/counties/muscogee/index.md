---
type: Jurisdiction
title: "Muscogee County, GA"
classification: county
fips: "13215"
state: "GA"
demographics:
  population: 203711
  population_under_18: 50790
  population_18_64: 122829
  population_65_plus: 30092
  median_household_income: 58073
  poverty_rate: 19.05
  homeownership_rate: 50.84
  unemployment_rate: 6.26
  median_home_value: 193900
  gini_index: 0.4911
  vacancy_rate: 11.54
  race_white: 77525
  race_black: 95710
  race_asian: 5550
  race_native: 355
  hispanic: 17357
  bachelors_plus: 57606
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 0.8319
  - to: "us/states/ga/districts/03"
    rel: in-district
    area_weight: 0.161
  - to: "us/states/ga/districts/senate/15"
    rel: in-district
    area_weight: 0.5973
  - to: "us/states/ga/districts/senate/29"
    rel: in-district
    area_weight: 0.4018
  - to: "us/states/ga/districts/house/137"
    rel: in-district
    area_weight: 0.4791
  - to: "us/states/ga/districts/house/141"
    rel: in-district
    area_weight: 0.1496
  - to: "us/states/ga/districts/house/139"
    rel: in-district
    area_weight: 0.1283
  - to: "us/states/ga/districts/house/140"
    rel: in-district
    area_weight: 0.1224
  - to: "us/states/ga/districts/house/138"
    rel: in-district
    area_weight: 0.1192
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Muscogee County, GA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 203711 |
| Under 18 | 50790 |
| 18–64 | 122829 |
| 65+ | 30092 |
| Median household income | 58073 |
| Poverty rate | 19.05 |
| Homeownership rate | 50.84 |
| Unemployment rate | 6.26 |
| Median home value | 193900 |
| Gini index | 0.4911 |
| Vacancy rate | 11.54 |
| White | 77525 |
| Black | 95710 |
| Asian | 5550 |
| Native | 355 |
| Hispanic/Latino | 17357 |
| Bachelor's or higher | 57606 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 83% (congressional)
- [GA-03](/us/states/ga/districts/03.md) — 16% (congressional)
- [GA Senate District 15](/us/states/ga/districts/senate/15.md) — 60% (state senate)
- [GA Senate District 29](/us/states/ga/districts/senate/29.md) — 40% (state senate)
- [GA House District 137](/us/states/ga/districts/house/137.md) — 48% (state house)
- [GA House District 141](/us/states/ga/districts/house/141.md) — 15% (state house)
- [GA House District 139](/us/states/ga/districts/house/139.md) — 13% (state house)
- [GA House District 140](/us/states/ga/districts/house/140.md) — 12% (state house)
- [GA House District 138](/us/states/ga/districts/house/138.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
