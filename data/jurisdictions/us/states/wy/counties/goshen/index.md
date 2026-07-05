---
type: Jurisdiction
title: "Goshen County, WY"
classification: county
fips: "56015"
state: "WY"
demographics:
  population: 12605
  population_under_18: 2473
  population_18_64: 7114
  population_65_plus: 3018
  median_household_income: 58929
  poverty_rate: 14.69
  homeownership_rate: 73.23
  unemployment_rate: 3.48
  median_home_value: 239600
  gini_index: 0.4722
  vacancy_rate: 11.2
  race_white: 10975
  race_black: 33
  race_asian: 119
  race_native: 92
  hispanic: 1288
  bachelors_plus: 2764
districts:
  - to: "us/states/wy/districts/00"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wy/districts/senate/3"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wy/districts/house/5"
    rel: in-district
    area_weight: 0.5879
  - to: "us/states/wy/districts/house/2"
    rel: in-district
    area_weight: 0.4119
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wy]
timestamp: "2026-07-03"
---

# Goshen County, WY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12605 |
| Under 18 | 2473 |
| 18–64 | 7114 |
| 65+ | 3018 |
| Median household income | 58929 |
| Poverty rate | 14.69 |
| Homeownership rate | 73.23 |
| Unemployment rate | 3.48 |
| Median home value | 239600 |
| Gini index | 0.4722 |
| Vacancy rate | 11.2 |
| White | 10975 |
| Black | 33 |
| Asian | 119 |
| Native | 92 |
| Hispanic/Latino | 1288 |
| Bachelor's or higher | 2764 |

## Districts

- [WY-00](/us/states/wy/districts/00.md) — 100% (congressional)
- [WY Senate District 3](/us/states/wy/districts/senate/3.md) — 100% (state senate)
- [WY House District 5](/us/states/wy/districts/house/5.md) — 59% (state house)
- [WY House District 2](/us/states/wy/districts/house/2.md) — 41% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
