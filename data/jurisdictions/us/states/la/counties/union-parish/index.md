---
type: Jurisdiction
title: "Union Parish, LA"
classification: county
fips: "22111"
state: "LA"
demographics:
  population: 20821
  population_under_18: 4484
  population_18_64: 11687
  population_65_plus: 4650
  median_household_income: 42885
  poverty_rate: 29.4
  homeownership_rate: 77.84
  unemployment_rate: 5.08
  median_home_value: 112500
  gini_index: 0.4863
  vacancy_rate: 18.44
  race_white: 14377
  race_black: 5037
  race_asian: 47
  race_native: 9
  hispanic: 1216
  bachelors_plus: 2770
districts:
  - to: "us/states/la/districts/04"
    rel: in-district
    area_weight: 0.9983
  - to: "us/states/la/districts/senate/33"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/la/districts/house/12"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Union Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20821 |
| Under 18 | 4484 |
| 18–64 | 11687 |
| 65+ | 4650 |
| Median household income | 42885 |
| Poverty rate | 29.4 |
| Homeownership rate | 77.84 |
| Unemployment rate | 5.08 |
| Median home value | 112500 |
| Gini index | 0.4863 |
| Vacancy rate | 18.44 |
| White | 14377 |
| Black | 5037 |
| Asian | 47 |
| Native | 9 |
| Hispanic/Latino | 1216 |
| Bachelor's or higher | 2770 |

## Districts

- [LA-04](/us/states/la/districts/04.md) — 100% (congressional)
- [LA Senate District 33](/us/states/la/districts/senate/33.md) — 100% (state senate)
- [LA House District 12](/us/states/la/districts/house/12.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
