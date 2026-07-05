---
type: Jurisdiction
title: "Box Elder County, UT"
classification: county
fips: "49003"
state: "UT"
demographics:
  population: 61246
  population_under_18: 18652
  population_18_64: 34629
  population_65_plus: 7965
  median_household_income: 84550
  poverty_rate: 8.41
  homeownership_rate: 75.97
  unemployment_rate: 3.25
  median_home_value: 403600
  gini_index: 0.3859
  vacancy_rate: 5.79
  race_white: 53715
  race_black: 207
  race_asian: 439
  race_native: 543
  hispanic: 6263
  bachelors_plus: 12492
districts:
  - to: "us/states/ut/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ut/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ut/districts/house/1"
    rel: in-district
    area_weight: 0.9898
  - to: "us/states/ut/districts/house/6"
    rel: in-district
    area_weight: 0.0102
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ut]
timestamp: "2026-07-03"
---

# Box Elder County, UT

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 61246 |
| Under 18 | 18652 |
| 18–64 | 34629 |
| 65+ | 7965 |
| Median household income | 84550 |
| Poverty rate | 8.41 |
| Homeownership rate | 75.97 |
| Unemployment rate | 3.25 |
| Median home value | 403600 |
| Gini index | 0.3859 |
| Vacancy rate | 5.79 |
| White | 53715 |
| Black | 207 |
| Asian | 439 |
| Native | 543 |
| Hispanic/Latino | 6263 |
| Bachelor's or higher | 12492 |

## Districts

- [UT-01](/us/states/ut/districts/01.md) — 100% (congressional)
- [UT Senate District 1](/us/states/ut/districts/senate/1.md) — 100% (state senate)
- [UT House District 1](/us/states/ut/districts/house/1.md) — 99% (state house)
- [UT House District 6](/us/states/ut/districts/house/6.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
