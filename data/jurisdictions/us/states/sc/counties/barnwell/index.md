---
type: Jurisdiction
title: "Barnwell County, SC"
classification: county
fips: "45011"
state: "SC"
demographics:
  population: 20521
  population_under_18: 4870
  population_18_64: 11724
  population_65_plus: 3927
  median_household_income: 46626
  poverty_rate: 25.01
  homeownership_rate: 70.93
  unemployment_rate: 7.05
  median_home_value: 106000
  gini_index: 0.4937
  vacancy_rate: 18.24
  race_white: 10716
  race_black: 8783
  race_asian: 120
  race_native: 25
  hispanic: 595
  bachelors_plus: 2710
districts:
  - to: "us/states/sc/districts/02"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/sc/districts/senate/40"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/sc/districts/house/91"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Barnwell County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20521 |
| Under 18 | 4870 |
| 18–64 | 11724 |
| 65+ | 3927 |
| Median household income | 46626 |
| Poverty rate | 25.01 |
| Homeownership rate | 70.93 |
| Unemployment rate | 7.05 |
| Median home value | 106000 |
| Gini index | 0.4937 |
| Vacancy rate | 18.24 |
| White | 10716 |
| Black | 8783 |
| Asian | 120 |
| Native | 25 |
| Hispanic/Latino | 595 |
| Bachelor's or higher | 2710 |

## Districts

- [SC-02](/us/states/sc/districts/02.md) — 100% (congressional)
- [SC Senate District 40](/us/states/sc/districts/senate/40.md) — 100% (state senate)
- [SC House District 91](/us/states/sc/districts/house/91.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
