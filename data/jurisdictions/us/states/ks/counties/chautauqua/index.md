---
type: Jurisdiction
title: "Chautauqua County, KS"
classification: county
fips: "20019"
state: "KS"
demographics:
  population: 3370
  population_under_18: 741
  population_18_64: 1819
  population_65_plus: 810
  median_household_income: 56438
  poverty_rate: 14.92
  homeownership_rate: 82.01
  unemployment_rate: 3.62
  median_home_value: 65500
  gini_index: 0.4601
  vacancy_rate: 31.34
  race_white: 2737
  race_black: 28
  race_asian: 3
  race_native: 168
  hispanic: 167
  bachelors_plus: 555
districts:
  - to: "us/states/ks/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/senate/15"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/12"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Chautauqua County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3370 |
| Under 18 | 741 |
| 18–64 | 1819 |
| 65+ | 810 |
| Median household income | 56438 |
| Poverty rate | 14.92 |
| Homeownership rate | 82.01 |
| Unemployment rate | 3.62 |
| Median home value | 65500 |
| Gini index | 0.4601 |
| Vacancy rate | 31.34 |
| White | 2737 |
| Black | 28 |
| Asian | 3 |
| Native | 168 |
| Hispanic/Latino | 167 |
| Bachelor's or higher | 555 |

## Districts

- [KS-04](/us/states/ks/districts/04.md) — 100% (congressional)
- [KS Senate District 15](/us/states/ks/districts/senate/15.md) — 100% (state senate)
- [KS House District 12](/us/states/ks/districts/house/12.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
