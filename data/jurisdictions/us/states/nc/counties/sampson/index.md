---
type: Jurisdiction
title: "Sampson County, NC"
classification: county
fips: "37163"
state: "NC"
demographics:
  population: 59470
  population_under_18: 14584
  population_18_64: 34093
  population_65_plus: 10793
  median_household_income: 52432
  poverty_rate: 21.82
  homeownership_rate: 73.81
  unemployment_rate: 5.27
  median_home_value: 150700
  gini_index: 0.4508
  vacancy_rate: 16.42
  race_white: 30375
  race_black: 14323
  race_asian: 255
  race_native: 1230
  hispanic: 13098
  bachelors_plus: 8318
districts:
  - to: "us/states/nc/districts/03"
    rel: in-district
    area_weight: 0.8107
  - to: "us/states/nc/districts/07"
    rel: in-district
    area_weight: 0.189
  - to: "us/states/nc/districts/senate/9"
    rel: in-district
    area_weight: 0.9591
  - to: "us/states/nc/districts/senate/12"
    rel: in-district
    area_weight: 0.0408
  - to: "us/states/nc/districts/house/22"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Sampson County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 59470 |
| Under 18 | 14584 |
| 18–64 | 34093 |
| 65+ | 10793 |
| Median household income | 52432 |
| Poverty rate | 21.82 |
| Homeownership rate | 73.81 |
| Unemployment rate | 5.27 |
| Median home value | 150700 |
| Gini index | 0.4508 |
| Vacancy rate | 16.42 |
| White | 30375 |
| Black | 14323 |
| Asian | 255 |
| Native | 1230 |
| Hispanic/Latino | 13098 |
| Bachelor's or higher | 8318 |

## Districts

- [NC-03](/us/states/nc/districts/03.md) — 81% (congressional)
- [NC-07](/us/states/nc/districts/07.md) — 19% (congressional)
- [NC Senate District 9](/us/states/nc/districts/senate/9.md) — 96% (state senate)
- [NC Senate District 12](/us/states/nc/districts/senate/12.md) — 4% (state senate)
- [NC House District 22](/us/states/nc/districts/house/22.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
