---
type: Jurisdiction
title: "Comanche County, OK"
classification: county
fips: "40031"
state: "OK"
demographics:
  population: 121825
  population_under_18: 29029
  population_18_64: 75984
  population_65_plus: 16812
  median_household_income: 60761
  poverty_rate: 18.09
  homeownership_rate: 55.6
  unemployment_rate: 7.07
  median_home_value: 163800
  gini_index: 0.4424
  vacancy_rate: 14.75
  race_white: 70201
  race_black: 18006
  race_asian: 3351
  race_native: 5918
  hispanic: 17883
  bachelors_plus: 25638
districts:
  - to: "us/states/ok/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/senate/32"
    rel: in-district
    area_weight: 0.5439
  - to: "us/states/ok/districts/senate/31"
    rel: in-district
    area_weight: 0.456
  - to: "us/states/ok/districts/house/63"
    rel: in-district
    area_weight: 0.6244
  - to: "us/states/ok/districts/house/65"
    rel: in-district
    area_weight: 0.2642
  - to: "us/states/ok/districts/house/64"
    rel: in-district
    area_weight: 0.0941
  - to: "us/states/ok/districts/house/62"
    rel: in-district
    area_weight: 0.0173
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Comanche County, OK

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 121825 |
| Under 18 | 29029 |
| 18–64 | 75984 |
| 65+ | 16812 |
| Median household income | 60761 |
| Poverty rate | 18.09 |
| Homeownership rate | 55.6 |
| Unemployment rate | 7.07 |
| Median home value | 163800 |
| Gini index | 0.4424 |
| Vacancy rate | 14.75 |
| White | 70201 |
| Black | 18006 |
| Asian | 3351 |
| Native | 5918 |
| Hispanic/Latino | 17883 |
| Bachelor's or higher | 25638 |

## Districts

- [OK-04](/us/states/ok/districts/04.md) — 100% (congressional)
- [OK Senate District 32](/us/states/ok/districts/senate/32.md) — 54% (state senate)
- [OK Senate District 31](/us/states/ok/districts/senate/31.md) — 46% (state senate)
- [OK House District 63](/us/states/ok/districts/house/63.md) — 62% (state house)
- [OK House District 65](/us/states/ok/districts/house/65.md) — 26% (state house)
- [OK House District 64](/us/states/ok/districts/house/64.md) — 9% (state house)
- [OK House District 62](/us/states/ok/districts/house/62.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
