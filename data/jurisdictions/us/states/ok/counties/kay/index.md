---
type: Jurisdiction
title: "Kay County, OK"
classification: county
fips: "40071"
state: "OK"
demographics:
  population: 43625
  population_under_18: 10822
  population_18_64: 24355
  population_65_plus: 8448
  median_household_income: 58423
  poverty_rate: 16.0
  homeownership_rate: 69.2
  unemployment_rate: 5.8
  median_home_value: 124700
  gini_index: 0.4443
  vacancy_rate: 19.78
  race_white: 32338
  race_black: 864
  race_asian: 231
  race_native: 3240
  hispanic: 3932
  bachelors_plus: 7369
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/senate/10"
    rel: in-district
    area_weight: 0.6058
  - to: "us/states/ok/districts/senate/19"
    rel: in-district
    area_weight: 0.3941
  - to: "us/states/ok/districts/house/38"
    rel: in-district
    area_weight: 0.6706
  - to: "us/states/ok/districts/house/37"
    rel: in-district
    area_weight: 0.3294
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Kay County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43625 |
| Under 18 | 10822 |
| 18–64 | 24355 |
| 65+ | 8448 |
| Median household income | 58423 |
| Poverty rate | 16.0 |
| Homeownership rate | 69.2 |
| Unemployment rate | 5.8 |
| Median home value | 124700 |
| Gini index | 0.4443 |
| Vacancy rate | 19.78 |
| White | 32338 |
| Black | 864 |
| Asian | 231 |
| Native | 3240 |
| Hispanic/Latino | 3932 |
| Bachelor's or higher | 7369 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 10](/us/states/ok/districts/senate/10.md) — 61% (state senate)
- [OK Senate District 19](/us/states/ok/districts/senate/19.md) — 39% (state senate)
- [OK House District 38](/us/states/ok/districts/house/38.md) — 67% (state house)
- [OK House District 37](/us/states/ok/districts/house/37.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
