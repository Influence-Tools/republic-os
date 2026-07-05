---
type: Jurisdiction
title: "Taylor County, GA"
classification: county
fips: "13269"
state: "GA"
demographics:
  population: 7786
  population_under_18: 1538
  population_18_64: 4539
  population_65_plus: 1709
  median_household_income: 41788
  poverty_rate: 32.06
  homeownership_rate: 62.88
  unemployment_rate: 2.55
  median_home_value: 87700
  gini_index: 0.5159
  vacancy_rate: 19.27
  race_white: 4557
  race_black: 2944
  race_asian: 23
  race_native: 31
  hispanic: 77
  bachelors_plus: 1414
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/ga/districts/senate/15"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ga/districts/house/150"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Taylor County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7786 |
| Under 18 | 1538 |
| 18–64 | 4539 |
| 65+ | 1709 |
| Median household income | 41788 |
| Poverty rate | 32.06 |
| Homeownership rate | 62.88 |
| Unemployment rate | 2.55 |
| Median home value | 87700 |
| Gini index | 0.5159 |
| Vacancy rate | 19.27 |
| White | 4557 |
| Black | 2944 |
| Asian | 23 |
| Native | 31 |
| Hispanic/Latino | 77 |
| Bachelor's or higher | 1414 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA Senate District 15](/us/states/ga/districts/senate/15.md) — 100% (state senate)
- [GA House District 150](/us/states/ga/districts/house/150.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
