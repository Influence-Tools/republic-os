---
type: Jurisdiction
title: "Platte County, MO"
classification: county
fips: "29165"
state: "MO"
demographics:
  population: 110371
  population_under_18: 25483
  population_18_64: 67132
  population_65_plus: 17756
  median_household_income: 96227
  poverty_rate: 7.02
  homeownership_rate: 67.36
  unemployment_rate: 2.7
  median_home_value: 345100
  gini_index: 0.4387
  vacancy_rate: 5.8
  race_white: 86796
  race_black: 8533
  race_asian: 2807
  race_native: 295
  hispanic: 7893
  bachelors_plus: 49140
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/senate/34"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/13"
    rel: in-district
    area_weight: 0.8484
  - to: "us/states/mo/districts/house/12"
    rel: in-district
    area_weight: 0.0852
  - to: "us/states/mo/districts/house/14"
    rel: in-district
    area_weight: 0.0663
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Platte County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 110371 |
| Under 18 | 25483 |
| 18–64 | 67132 |
| 65+ | 17756 |
| Median household income | 96227 |
| Poverty rate | 7.02 |
| Homeownership rate | 67.36 |
| Unemployment rate | 2.7 |
| Median home value | 345100 |
| Gini index | 0.4387 |
| Vacancy rate | 5.8 |
| White | 86796 |
| Black | 8533 |
| Asian | 2807 |
| Native | 295 |
| Hispanic/Latino | 7893 |
| Bachelor's or higher | 49140 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 100% (congressional)
- [MO Senate District 34](/us/states/mo/districts/senate/34.md) — 100% (state senate)
- [MO House District 13](/us/states/mo/districts/house/13.md) — 85% (state house)
- [MO House District 12](/us/states/mo/districts/house/12.md) — 9% (state house)
- [MO House District 14](/us/states/mo/districts/house/14.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
