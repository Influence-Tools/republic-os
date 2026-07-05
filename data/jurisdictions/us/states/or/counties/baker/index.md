---
type: Jurisdiction
title: "Baker County, OR"
classification: county
fips: "41001"
state: "OR"
demographics:
  population: 16840
  population_under_18: 3328
  population_18_64: 8780
  population_65_plus: 4732
  median_household_income: 60936
  poverty_rate: 14.85
  homeownership_rate: 71.49
  unemployment_rate: 5.63
  median_home_value: 285600
  gini_index: 0.4417
  vacancy_rate: 15.7
  race_white: 14973
  race_black: 222
  race_asian: 63
  race_native: 172
  hispanic: 896
  bachelors_plus: 4211
districts:
  - to: "us/states/or/districts/02"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/or/districts/senate/30"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/or/districts/house/60"
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

# Baker County, OR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16840 |
| Under 18 | 3328 |
| 18–64 | 8780 |
| 65+ | 4732 |
| Median household income | 60936 |
| Poverty rate | 14.85 |
| Homeownership rate | 71.49 |
| Unemployment rate | 5.63 |
| Median home value | 285600 |
| Gini index | 0.4417 |
| Vacancy rate | 15.7 |
| White | 14973 |
| Black | 222 |
| Asian | 63 |
| Native | 172 |
| Hispanic/Latino | 896 |
| Bachelor's or higher | 4211 |

## Districts

- [OR-02](/us/states/or/districts/02.md) — 100% (congressional)
- [OR Senate District 30](/us/states/or/districts/senate/30.md) — 100% (state senate)
- [OR House District 60](/us/states/or/districts/house/60.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
