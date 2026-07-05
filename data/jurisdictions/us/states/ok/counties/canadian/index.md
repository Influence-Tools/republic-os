---
type: Jurisdiction
title: "Canadian County, OK"
classification: county
fips: "40017"
state: "OK"
demographics:
  population: 168985
  population_under_18: 43344
  population_18_64: 102561
  population_65_plus: 23080
  median_household_income: 87751
  poverty_rate: 8.04
  homeownership_rate: 74.81
  unemployment_rate: 4.45
  median_home_value: 246200
  gini_index: 0.3922
  vacancy_rate: 6.02
  race_white: 122750
  race_black: 6586
  race_asian: 5289
  race_native: 5887
  hispanic: 20269
  bachelors_plus: 46822
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 0.8138
  - to: "us/states/ok/districts/05"
    rel: in-district
    area_weight: 0.1854
  - to: "us/states/ok/districts/senate/26"
    rel: in-district
    area_weight: 0.5027
  - to: "us/states/ok/districts/senate/23"
    rel: in-district
    area_weight: 0.2945
  - to: "us/states/ok/districts/senate/22"
    rel: in-district
    area_weight: 0.1094
  - to: "us/states/ok/districts/senate/18"
    rel: in-district
    area_weight: 0.0671
  - to: "us/states/ok/districts/senate/45"
    rel: in-district
    area_weight: 0.0241
  - to: "us/states/ok/districts/house/55"
    rel: in-district
    area_weight: 0.3638
  - to: "us/states/ok/districts/house/56"
    rel: in-district
    area_weight: 0.3059
  - to: "us/states/ok/districts/house/60"
    rel: in-district
    area_weight: 0.1552
  - to: "us/states/ok/districts/house/41"
    rel: in-district
    area_weight: 0.0816
  - to: "us/states/ok/districts/house/47"
    rel: in-district
    area_weight: 0.0775
  - to: "us/states/ok/districts/house/43"
    rel: in-district
    area_weight: 0.0161
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Canadian County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 168985 |
| Under 18 | 43344 |
| 18–64 | 102561 |
| 65+ | 23080 |
| Median household income | 87751 |
| Poverty rate | 8.04 |
| Homeownership rate | 74.81 |
| Unemployment rate | 4.45 |
| Median home value | 246200 |
| Gini index | 0.3922 |
| Vacancy rate | 6.02 |
| White | 122750 |
| Black | 6586 |
| Asian | 5289 |
| Native | 5887 |
| Hispanic/Latino | 20269 |
| Bachelor's or higher | 46822 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 81% (congressional)
- [OK-05](/us/states/ok/districts/05.md) — 19% (congressional)
- [OK Senate District 26](/us/states/ok/districts/senate/26.md) — 50% (state senate)
- [OK Senate District 23](/us/states/ok/districts/senate/23.md) — 29% (state senate)
- [OK Senate District 22](/us/states/ok/districts/senate/22.md) — 11% (state senate)
- [OK Senate District 18](/us/states/ok/districts/senate/18.md) — 7% (state senate)
- [OK Senate District 45](/us/states/ok/districts/senate/45.md) — 2% (state senate)
- [OK House District 55](/us/states/ok/districts/house/55.md) — 36% (state house)
- [OK House District 56](/us/states/ok/districts/house/56.md) — 31% (state house)
- [OK House District 60](/us/states/ok/districts/house/60.md) — 16% (state house)
- [OK House District 41](/us/states/ok/districts/house/41.md) — 8% (state house)
- [OK House District 47](/us/states/ok/districts/house/47.md) — 8% (state house)
- [OK House District 43](/us/states/ok/districts/house/43.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
