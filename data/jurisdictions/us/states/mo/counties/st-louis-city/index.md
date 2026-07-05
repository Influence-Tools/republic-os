---
type: Jurisdiction
title: "St. Louis city, MO"
classification: county
fips: "29510"
state: "MO"
demographics:
  population: 288512
  population_under_18: 52870
  population_18_64: 190935
  population_65_plus: 44707
  median_household_income: 56160
  poverty_rate: 20.64
  homeownership_rate: 45.28
  unemployment_rate: 5.05
  median_home_value: 197500
  gini_index: 0.5034
  vacancy_rate: 16.78
  race_white: 131235
  race_black: 121932
  race_asian: 10200
  race_native: 723
  hispanic: 15297
  bachelors_plus: 125836
districts:
  - to: "us/states/mo/districts/01"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/mo/districts/senate/5"
    rel: in-district
    area_weight: 0.6813
  - to: "us/states/mo/districts/senate/4"
    rel: in-district
    area_weight: 0.3184
  - to: "us/states/mo/districts/house/76"
    rel: in-district
    area_weight: 0.2914
  - to: "us/states/mo/districts/house/84"
    rel: in-district
    area_weight: 0.1401
  - to: "us/states/mo/districts/house/79"
    rel: in-district
    area_weight: 0.1088
  - to: "us/states/mo/districts/house/82"
    rel: in-district
    area_weight: 0.108
  - to: "us/states/mo/districts/house/81"
    rel: in-district
    area_weight: 0.104
  - to: "us/states/mo/districts/house/77"
    rel: in-district
    area_weight: 0.0988
  - to: "us/states/mo/districts/house/78"
    rel: in-district
    area_weight: 0.0762
  - to: "us/states/mo/districts/house/80"
    rel: in-district
    area_weight: 0.0724
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# St. Louis city, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 288512 |
| Under 18 | 52870 |
| 18–64 | 190935 |
| 65+ | 44707 |
| Median household income | 56160 |
| Poverty rate | 20.64 |
| Homeownership rate | 45.28 |
| Unemployment rate | 5.05 |
| Median home value | 197500 |
| Gini index | 0.5034 |
| Vacancy rate | 16.78 |
| White | 131235 |
| Black | 121932 |
| Asian | 10200 |
| Native | 723 |
| Hispanic/Latino | 15297 |
| Bachelor's or higher | 125836 |

## Districts

- [MO-01](/us/states/mo/districts/01.md) — 100% (congressional)
- [MO Senate District 5](/us/states/mo/districts/senate/5.md) — 68% (state senate)
- [MO Senate District 4](/us/states/mo/districts/senate/4.md) — 32% (state senate)
- [MO House District 76](/us/states/mo/districts/house/76.md) — 29% (state house)
- [MO House District 84](/us/states/mo/districts/house/84.md) — 14% (state house)
- [MO House District 79](/us/states/mo/districts/house/79.md) — 11% (state house)
- [MO House District 82](/us/states/mo/districts/house/82.md) — 11% (state house)
- [MO House District 81](/us/states/mo/districts/house/81.md) — 10% (state house)
- [MO House District 77](/us/states/mo/districts/house/77.md) — 10% (state house)
- [MO House District 78](/us/states/mo/districts/house/78.md) — 8% (state house)
- [MO House District 80](/us/states/mo/districts/house/80.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
