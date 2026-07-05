---
type: Jurisdiction
title: "Owsley County, KY"
classification: county
fips: "21189"
state: "KY"
demographics:
  population: 3971
  population_under_18: 766
  population_18_64: 2389
  population_65_plus: 816
  median_household_income: 22188
  poverty_rate: 36.15
  homeownership_rate: 70.13
  unemployment_rate: 12.58
  median_home_value: 80100
  gini_index: 0.5624
  vacancy_rate: 23.64
  race_white: 3794
  race_black: 0
  race_asian: 7
  race_native: 0
  hispanic: 3
  bachelors_plus: 273
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/25"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ky/districts/house/84"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Owsley County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3971 |
| Under 18 | 766 |
| 18–64 | 2389 |
| 65+ | 816 |
| Median household income | 22188 |
| Poverty rate | 36.15 |
| Homeownership rate | 70.13 |
| Unemployment rate | 12.58 |
| Median home value | 80100 |
| Gini index | 0.5624 |
| Vacancy rate | 23.64 |
| White | 3794 |
| Black | 0 |
| Asian | 7 |
| Native | 0 |
| Hispanic/Latino | 3 |
| Bachelor's or higher | 273 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 25](/us/states/ky/districts/senate/25.md) — 100% (state senate)
- [KY House District 84](/us/states/ky/districts/house/84.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
