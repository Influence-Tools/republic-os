---
type: Jurisdiction
title: "Rogers County, OK"
classification: county
fips: "40131"
state: "OK"
demographics:
  population: 98610
  population_under_18: 22887
  population_18_64: 58723
  population_65_plus: 17000
  median_household_income: 80067
  poverty_rate: 8.85
  homeownership_rate: 77.75
  unemployment_rate: 4.74
  median_home_value: 240500
  gini_index: 0.4232
  vacancy_rate: 6.85
  race_white: 69557
  race_black: 938
  race_asian: 1835
  race_native: 12492
  hispanic: 6085
  bachelors_plus: 24076
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 0.947
  - to: "us/states/ok/districts/01"
    rel: in-district
    area_weight: 0.053
  - to: "us/states/ok/districts/senate/29"
    rel: in-district
    area_weight: 0.458
  - to: "us/states/ok/districts/senate/2"
    rel: in-district
    area_weight: 0.3862
  - to: "us/states/ok/districts/senate/3"
    rel: in-district
    area_weight: 0.0951
  - to: "us/states/ok/districts/senate/1"
    rel: in-district
    area_weight: 0.0606
  - to: "us/states/ok/districts/house/6"
    rel: in-district
    area_weight: 0.5095
  - to: "us/states/ok/districts/house/8"
    rel: in-district
    area_weight: 0.2748
  - to: "us/states/ok/districts/house/23"
    rel: in-district
    area_weight: 0.1093
  - to: "us/states/ok/districts/house/9"
    rel: in-district
    area_weight: 0.0873
  - to: "us/states/ok/districts/house/74"
    rel: in-district
    area_weight: 0.0191
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Rogers County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 98610 |
| Under 18 | 22887 |
| 18–64 | 58723 |
| 65+ | 17000 |
| Median household income | 80067 |
| Poverty rate | 8.85 |
| Homeownership rate | 77.75 |
| Unemployment rate | 4.74 |
| Median home value | 240500 |
| Gini index | 0.4232 |
| Vacancy rate | 6.85 |
| White | 69557 |
| Black | 938 |
| Asian | 1835 |
| Native | 12492 |
| Hispanic/Latino | 6085 |
| Bachelor's or higher | 24076 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 95% (congressional)
- [OK-01](/us/states/ok/districts/01.md) — 5% (congressional)
- [OK Senate District 29](/us/states/ok/districts/senate/29.md) — 46% (state senate)
- [OK Senate District 2](/us/states/ok/districts/senate/2.md) — 39% (state senate)
- [OK Senate District 3](/us/states/ok/districts/senate/3.md) — 10% (state senate)
- [OK Senate District 1](/us/states/ok/districts/senate/1.md) — 6% (state senate)
- [OK House District 6](/us/states/ok/districts/house/6.md) — 51% (state house)
- [OK House District 8](/us/states/ok/districts/house/8.md) — 27% (state house)
- [OK House District 23](/us/states/ok/districts/house/23.md) — 11% (state house)
- [OK House District 9](/us/states/ok/districts/house/9.md) — 9% (state house)
- [OK House District 74](/us/states/ok/districts/house/74.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
