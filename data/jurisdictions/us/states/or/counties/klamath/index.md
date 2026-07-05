---
type: Jurisdiction
title: "Klamath County, OR"
classification: county
fips: "41035"
state: "OR"
demographics:
  population: 70247
  population_under_18: 15216
  population_18_64: 39336
  population_65_plus: 15695
  median_household_income: 58830
  poverty_rate: 18.31
  homeownership_rate: 69.42
  unemployment_rate: 7.18
  median_home_value: 280400
  gini_index: 0.4847
  vacancy_rate: 12.55
  race_white: 54261
  race_black: 534
  race_asian: 726
  race_native: 1929
  hispanic: 9748
  bachelors_plus: 15371
districts:
  - to: "us/states/or/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/or/districts/senate/28"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/or/districts/house/55"
    rel: in-district
    area_weight: 0.7877
  - to: "us/states/or/districts/house/56"
    rel: in-district
    area_weight: 0.2121
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Klamath County, OR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 70247 |
| Under 18 | 15216 |
| 18–64 | 39336 |
| 65+ | 15695 |
| Median household income | 58830 |
| Poverty rate | 18.31 |
| Homeownership rate | 69.42 |
| Unemployment rate | 7.18 |
| Median home value | 280400 |
| Gini index | 0.4847 |
| Vacancy rate | 12.55 |
| White | 54261 |
| Black | 534 |
| Asian | 726 |
| Native | 1929 |
| Hispanic/Latino | 9748 |
| Bachelor's or higher | 15371 |

## Districts

- [OR-02](/us/states/or/districts/02.md) — 100% (congressional)
- [OR Senate District 28](/us/states/or/districts/senate/28.md) — 100% (state senate)
- [OR House District 55](/us/states/or/districts/house/55.md) — 79% (state house)
- [OR House District 56](/us/states/or/districts/house/56.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
