---
type: Jurisdiction
title: "Sutter County, CA"
classification: county
fips: "06101"
state: "CA"
demographics:
  population: 98857
  population_under_18: 24874
  population_18_64: 57767
  population_65_plus: 16216
  median_household_income: 79704
  poverty_rate: 14.43
  homeownership_rate: 61.33
  unemployment_rate: 7.16
  median_home_value: 433500
  gini_index: 0.4635
  vacancy_rate: 4.33
  race_white: 44686
  race_black: 1804
  race_asian: 17555
  race_native: 1900
  hispanic: 32532
  bachelors_plus: 17921
districts:
  - to: "us/states/ca/districts/01"
    rel: in-district
    area_weight: 0.9973
  - to: "us/states/ca/districts/senate/1"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ca/districts/house/3"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Sutter County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 98857 |
| Under 18 | 24874 |
| 18–64 | 57767 |
| 65+ | 16216 |
| Median household income | 79704 |
| Poverty rate | 14.43 |
| Homeownership rate | 61.33 |
| Unemployment rate | 7.16 |
| Median home value | 433500 |
| Gini index | 0.4635 |
| Vacancy rate | 4.33 |
| White | 44686 |
| Black | 1804 |
| Asian | 17555 |
| Native | 1900 |
| Hispanic/Latino | 32532 |
| Bachelor's or higher | 17921 |

## Districts

- [CA-01](/us/states/ca/districts/01.md) — 100% (congressional)
- [CA Senate District 1](/us/states/ca/districts/senate/1.md) — 100% (state senate)
- [CA House District 3](/us/states/ca/districts/house/3.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
