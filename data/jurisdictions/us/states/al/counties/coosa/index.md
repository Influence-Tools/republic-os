---
type: Jurisdiction
title: "Coosa County, AL"
classification: county
fips: "01037"
state: "AL"
demographics:
  population: 10300
  population_under_18: 1795
  population_18_64: 5898
  population_65_plus: 2607
  median_household_income: 57355
  poverty_rate: 13.13
  homeownership_rate: 81.58
  unemployment_rate: 6.2
  median_home_value: 115500
  gini_index: 0.3977
  vacancy_rate: 27.07
  race_white: 6806
  race_black: 3007
  race_asian: 29
  race_native: 7
  hispanic: 253
  bachelors_plus: 1467
districts:
  - to: "us/states/al/districts/06"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/al/districts/senate/30"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/al/districts/house/33"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Coosa County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10300 |
| Under 18 | 1795 |
| 18–64 | 5898 |
| 65+ | 2607 |
| Median household income | 57355 |
| Poverty rate | 13.13 |
| Homeownership rate | 81.58 |
| Unemployment rate | 6.2 |
| Median home value | 115500 |
| Gini index | 0.3977 |
| Vacancy rate | 27.07 |
| White | 6806 |
| Black | 3007 |
| Asian | 29 |
| Native | 7 |
| Hispanic/Latino | 253 |
| Bachelor's or higher | 1467 |

## Districts

- [AL-06](/us/states/al/districts/06.md) — 100% (congressional)
- [AL Senate District 30](/us/states/al/districts/senate/30.md) — 100% (state senate)
- [AL House District 33](/us/states/al/districts/house/33.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
