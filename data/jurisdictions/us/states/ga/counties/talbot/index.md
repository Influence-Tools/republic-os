---
type: Jurisdiction
title: "Talbot County, GA"
classification: county
fips: "13263"
state: "GA"
demographics:
  population: 5742
  population_under_18: 946
  population_18_64: 3223
  population_65_plus: 1573
  median_household_income: 41597
  poverty_rate: 25.23
  homeownership_rate: 79.56
  unemployment_rate: 3.3
  median_home_value: 117100
  gini_index: 0.4964
  vacancy_rate: 17.3
  race_white: 2319
  race_black: 3083
  race_asian: 4
  race_native: 1
  hispanic: 36
  bachelors_plus: 723
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 0.9959
  - to: "us/states/ga/districts/senate/15"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/137"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Talbot County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5742 |
| Under 18 | 946 |
| 18–64 | 3223 |
| 65+ | 1573 |
| Median household income | 41597 |
| Poverty rate | 25.23 |
| Homeownership rate | 79.56 |
| Unemployment rate | 3.3 |
| Median home value | 117100 |
| Gini index | 0.4964 |
| Vacancy rate | 17.3 |
| White | 2319 |
| Black | 3083 |
| Asian | 4 |
| Native | 1 |
| Hispanic/Latino | 36 |
| Bachelor's or higher | 723 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA Senate District 15](/us/states/ga/districts/senate/15.md) — 100% (state senate)
- [GA House District 137](/us/states/ga/districts/house/137.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
