---
type: Jurisdiction
title: "Wagoner County, OK"
classification: county
fips: "40145"
state: "OK"
demographics:
  population: 86609
  population_under_18: 20460
  population_18_64: 51352
  population_65_plus: 14797
  median_household_income: 81207
  poverty_rate: 9.2
  homeownership_rate: 81.26
  unemployment_rate: 4.22
  median_home_value: 234800
  gini_index: 0.4074
  vacancy_rate: 8.19
  race_white: 59254
  race_black: 2961
  race_asian: 1903
  race_native: 7240
  hispanic: 7584
  bachelors_plus: 21832
districts:
  - to: "us/states/ok/districts/01"
    rel: in-district
    area_weight: 0.5907
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 0.4093
  - to: "us/states/ok/districts/senate/3"
    rel: in-district
    area_weight: 0.9182
  - to: "us/states/ok/districts/senate/36"
    rel: in-district
    area_weight: 0.0817
  - to: "us/states/ok/districts/house/12"
    rel: in-district
    area_weight: 0.677
  - to: "us/states/ok/districts/house/14"
    rel: in-district
    area_weight: 0.126
  - to: "us/states/ok/districts/house/4"
    rel: in-district
    area_weight: 0.0528
  - to: "us/states/ok/districts/house/13"
    rel: in-district
    area_weight: 0.0457
  - to: "us/states/ok/districts/house/8"
    rel: in-district
    area_weight: 0.0428
  - to: "us/states/ok/districts/house/23"
    rel: in-district
    area_weight: 0.0308
  - to: "us/states/ok/districts/house/98"
    rel: in-district
    area_weight: 0.0249
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Wagoner County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 86609 |
| Under 18 | 20460 |
| 18–64 | 51352 |
| 65+ | 14797 |
| Median household income | 81207 |
| Poverty rate | 9.2 |
| Homeownership rate | 81.26 |
| Unemployment rate | 4.22 |
| Median home value | 234800 |
| Gini index | 0.4074 |
| Vacancy rate | 8.19 |
| White | 59254 |
| Black | 2961 |
| Asian | 1903 |
| Native | 7240 |
| Hispanic/Latino | 7584 |
| Bachelor's or higher | 21832 |

## Districts

- [OK-01](/us/states/ok/districts/01.md) — 59% (congressional)
- [OK-02](/us/states/ok/districts/02.md) — 41% (congressional)
- [OK Senate District 3](/us/states/ok/districts/senate/3.md) — 92% (state senate)
- [OK Senate District 36](/us/states/ok/districts/senate/36.md) — 8% (state senate)
- [OK House District 12](/us/states/ok/districts/house/12.md) — 68% (state house)
- [OK House District 14](/us/states/ok/districts/house/14.md) — 13% (state house)
- [OK House District 4](/us/states/ok/districts/house/4.md) — 5% (state house)
- [OK House District 13](/us/states/ok/districts/house/13.md) — 5% (state house)
- [OK House District 8](/us/states/ok/districts/house/8.md) — 4% (state house)
- [OK House District 23](/us/states/ok/districts/house/23.md) — 3% (state house)
- [OK House District 98](/us/states/ok/districts/house/98.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
