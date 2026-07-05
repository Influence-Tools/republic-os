---
type: Jurisdiction
title: "Payne County, OK"
classification: county
fips: "40119"
state: "OK"
demographics:
  population: 82972
  population_under_18: 15294
  population_18_64: 56765
  population_65_plus: 10913
  median_household_income: 49809
  poverty_rate: 22.6
  homeownership_rate: 51.03
  unemployment_rate: 5.73
  median_home_value: 223300
  gini_index: 0.5205
  vacancy_rate: 12.03
  race_white: 62563
  race_black: 3034
  race_asian: 3491
  race_native: 3417
  hispanic: 5450
  bachelors_plus: 26095
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/ok/districts/senate/21"
    rel: in-district
    area_weight: 0.6025
  - to: "us/states/ok/districts/senate/20"
    rel: in-district
    area_weight: 0.3975
  - to: "us/states/ok/districts/house/33"
    rel: in-district
    area_weight: 0.801
  - to: "us/states/ok/districts/house/35"
    rel: in-district
    area_weight: 0.1046
  - to: "us/states/ok/districts/house/32"
    rel: in-district
    area_weight: 0.0623
  - to: "us/states/ok/districts/house/34"
    rel: in-district
    area_weight: 0.0321
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Payne County, OK

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 82972 |
| Under 18 | 15294 |
| 18–64 | 56765 |
| 65+ | 10913 |
| Median household income | 49809 |
| Poverty rate | 22.6 |
| Homeownership rate | 51.03 |
| Unemployment rate | 5.73 |
| Median home value | 223300 |
| Gini index | 0.5205 |
| Vacancy rate | 12.03 |
| White | 62563 |
| Black | 3034 |
| Asian | 3491 |
| Native | 3417 |
| Hispanic/Latino | 5450 |
| Bachelor's or higher | 26095 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 21](/us/states/ok/districts/senate/21.md) — 60% (state senate)
- [OK Senate District 20](/us/states/ok/districts/senate/20.md) — 40% (state senate)
- [OK House District 33](/us/states/ok/districts/house/33.md) — 80% (state house)
- [OK House District 35](/us/states/ok/districts/house/35.md) — 10% (state house)
- [OK House District 32](/us/states/ok/districts/house/32.md) — 6% (state house)
- [OK House District 34](/us/states/ok/districts/house/34.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
