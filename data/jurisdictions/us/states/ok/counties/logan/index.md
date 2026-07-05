---
type: Jurisdiction
title: "Logan County, OK"
classification: county
fips: "40083"
state: "OK"
demographics:
  population: 51938
  population_under_18: 11421
  population_18_64: 31430
  population_65_plus: 9087
  median_household_income: 83899
  poverty_rate: 11.64
  homeownership_rate: 85.16
  unemployment_rate: 3.6
  median_home_value: 246700
  gini_index: 0.4593
  vacancy_rate: 8.44
  race_white: 39498
  race_black: 2986
  race_asian: 340
  race_native: 1518
  hispanic: 4664
  bachelors_plus: 14390
districts:
  - to: "us/states/ok/districts/05"
    rel: in-district
    area_weight: 0.5741
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 0.4259
  - to: "us/states/ok/districts/senate/20"
    rel: in-district
    area_weight: 0.8102
  - to: "us/states/ok/districts/senate/28"
    rel: in-district
    area_weight: 0.1898
  - to: "us/states/ok/districts/house/38"
    rel: in-district
    area_weight: 0.4895
  - to: "us/states/ok/districts/house/31"
    rel: in-district
    area_weight: 0.2318
  - to: "us/states/ok/districts/house/33"
    rel: in-district
    area_weight: 0.1392
  - to: "us/states/ok/districts/house/32"
    rel: in-district
    area_weight: 0.0858
  - to: "us/states/ok/districts/house/41"
    rel: in-district
    area_weight: 0.0536
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Logan County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 51938 |
| Under 18 | 11421 |
| 18–64 | 31430 |
| 65+ | 9087 |
| Median household income | 83899 |
| Poverty rate | 11.64 |
| Homeownership rate | 85.16 |
| Unemployment rate | 3.6 |
| Median home value | 246700 |
| Gini index | 0.4593 |
| Vacancy rate | 8.44 |
| White | 39498 |
| Black | 2986 |
| Asian | 340 |
| Native | 1518 |
| Hispanic/Latino | 4664 |
| Bachelor's or higher | 14390 |

## Districts

- [OK-05](/us/states/ok/districts/05.md) — 57% (congressional)
- [OK-03](/us/states/ok/districts/03.md) — 43% (congressional)
- [OK Senate District 20](/us/states/ok/districts/senate/20.md) — 81% (state senate)
- [OK Senate District 28](/us/states/ok/districts/senate/28.md) — 19% (state senate)
- [OK House District 38](/us/states/ok/districts/house/38.md) — 49% (state house)
- [OK House District 31](/us/states/ok/districts/house/31.md) — 23% (state house)
- [OK House District 33](/us/states/ok/districts/house/33.md) — 14% (state house)
- [OK House District 32](/us/states/ok/districts/house/32.md) — 9% (state house)
- [OK House District 41](/us/states/ok/districts/house/41.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
