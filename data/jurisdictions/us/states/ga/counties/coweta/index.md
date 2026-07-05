---
type: Jurisdiction
title: "Coweta County, GA"
classification: county
fips: "13077"
state: "GA"
demographics:
  population: 152852
  population_under_18: 35278
  population_18_64: 94356
  population_65_plus: 23218
  median_household_income: 95548
  poverty_rate: 7.42
  homeownership_rate: 78.41
  unemployment_rate: 3.09
  median_home_value: 357500
  gini_index: 0.4133
  vacancy_rate: 4.94
  race_white: 106346
  race_black: 28158
  race_asian: 3204
  race_native: 535
  hispanic: 12522
  bachelors_plus: 52416
districts:
  - to: "us/states/ga/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/senate/6"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ga/districts/house/136"
    rel: in-district
    area_weight: 0.4115
  - to: "us/states/ga/districts/house/70"
    rel: in-district
    area_weight: 0.3245
  - to: "us/states/ga/districts/house/65"
    rel: in-district
    area_weight: 0.1114
  - to: "us/states/ga/districts/house/73"
    rel: in-district
    area_weight: 0.0906
  - to: "us/states/ga/districts/house/67"
    rel: in-district
    area_weight: 0.0618
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Coweta County, GA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 152852 |
| Under 18 | 35278 |
| 18–64 | 94356 |
| 65+ | 23218 |
| Median household income | 95548 |
| Poverty rate | 7.42 |
| Homeownership rate | 78.41 |
| Unemployment rate | 3.09 |
| Median home value | 357500 |
| Gini index | 0.4133 |
| Vacancy rate | 4.94 |
| White | 106346 |
| Black | 28158 |
| Asian | 3204 |
| Native | 535 |
| Hispanic/Latino | 12522 |
| Bachelor's or higher | 52416 |

## Districts

- [GA-03](/us/states/ga/districts/03.md) — 100% (congressional)
- [GA Senate District 6](/us/states/ga/districts/senate/6.md) — 100% (state senate)
- [GA House District 136](/us/states/ga/districts/house/136.md) — 41% (state house)
- [GA House District 70](/us/states/ga/districts/house/70.md) — 32% (state house)
- [GA House District 65](/us/states/ga/districts/house/65.md) — 11% (state house)
- [GA House District 73](/us/states/ga/districts/house/73.md) — 9% (state house)
- [GA House District 67](/us/states/ga/districts/house/67.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
