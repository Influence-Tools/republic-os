---
type: Jurisdiction
title: "Jewell County, KS"
classification: county
fips: "20089"
state: "KS"
demographics:
  population: 2916
  population_under_18: 618
  population_18_64: 1384
  population_65_plus: 914
  median_household_income: 52634
  poverty_rate: 10.59
  homeownership_rate: 74.11
  unemployment_rate: 1.35
  median_home_value: 64600
  gini_index: 0.4533
  vacancy_rate: 25.21
  race_white: 2701
  race_black: 21
  race_asian: 13
  race_native: 6
  hispanic: 83
  bachelors_plus: 484
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/36"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/106"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Jewell County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2916 |
| Under 18 | 618 |
| 18–64 | 1384 |
| 65+ | 914 |
| Median household income | 52634 |
| Poverty rate | 10.59 |
| Homeownership rate | 74.11 |
| Unemployment rate | 1.35 |
| Median home value | 64600 |
| Gini index | 0.4533 |
| Vacancy rate | 25.21 |
| White | 2701 |
| Black | 21 |
| Asian | 13 |
| Native | 6 |
| Hispanic/Latino | 83 |
| Bachelor's or higher | 484 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 36](/us/states/ks/districts/senate/36.md) — 100% (state senate)
- [KS House District 106](/us/states/ks/districts/house/106.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
