---
type: Jurisdiction
title: "Union County, OR"
classification: county
fips: "41061"
state: "OR"
demographics:
  population: 26144
  population_under_18: 5591
  population_18_64: 14969
  population_65_plus: 5584
  median_household_income: 65661
  poverty_rate: 16.06
  homeownership_rate: 65.51
  unemployment_rate: 5.73
  median_home_value: 294600
  gini_index: 0.4647
  vacancy_rate: 7.85
  race_white: 22960
  race_black: 260
  race_asian: 326
  race_native: 154
  hispanic: 1441
  bachelors_plus: 6157
districts:
  - to: "us/states/or/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/or/districts/senate/29"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/or/districts/house/58"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Union County, OR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26144 |
| Under 18 | 5591 |
| 18–64 | 14969 |
| 65+ | 5584 |
| Median household income | 65661 |
| Poverty rate | 16.06 |
| Homeownership rate | 65.51 |
| Unemployment rate | 5.73 |
| Median home value | 294600 |
| Gini index | 0.4647 |
| Vacancy rate | 7.85 |
| White | 22960 |
| Black | 260 |
| Asian | 326 |
| Native | 154 |
| Hispanic/Latino | 1441 |
| Bachelor's or higher | 6157 |

## Districts

- [OR-02](/us/states/or/districts/02.md) — 100% (congressional)
- [OR Senate District 29](/us/states/or/districts/senate/29.md) — 100% (state senate)
- [OR House District 58](/us/states/or/districts/house/58.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
