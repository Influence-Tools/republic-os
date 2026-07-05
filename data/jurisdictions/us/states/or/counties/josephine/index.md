---
type: Jurisdiction
title: "Josephine County, OR"
classification: county
fips: "41033"
state: "OR"
demographics:
  population: 88179
  population_under_18: 16970
  population_18_64: 47210
  population_65_plus: 23999
  median_household_income: 60098
  poverty_rate: 15.59
  homeownership_rate: 71.72
  unemployment_rate: 6.4
  median_home_value: 404300
  gini_index: 0.4771
  vacancy_rate: 7.06
  race_white: 75554
  race_black: 367
  race_asian: 703
  race_native: 477
  hispanic: 7777
  bachelors_plus: 17702
districts:
  - to: "us/states/or/districts/02"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/or/districts/senate/2"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/or/districts/house/3"
    rel: in-district
    area_weight: 0.7682
  - to: "us/states/or/districts/house/4"
    rel: in-district
    area_weight: 0.2317
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Josephine County, OR

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 88179 |
| Under 18 | 16970 |
| 18–64 | 47210 |
| 65+ | 23999 |
| Median household income | 60098 |
| Poverty rate | 15.59 |
| Homeownership rate | 71.72 |
| Unemployment rate | 6.4 |
| Median home value | 404300 |
| Gini index | 0.4771 |
| Vacancy rate | 7.06 |
| White | 75554 |
| Black | 367 |
| Asian | 703 |
| Native | 477 |
| Hispanic/Latino | 7777 |
| Bachelor's or higher | 17702 |

## Districts

- [OR-02](/us/states/or/districts/02.md) — 100% (congressional)
- [OR Senate District 2](/us/states/or/districts/senate/2.md) — 100% (state senate)
- [OR House District 3](/us/states/or/districts/house/3.md) — 77% (state house)
- [OR House District 4](/us/states/or/districts/house/4.md) — 23% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
