---
type: Jurisdiction
title: "Dallas County, MO"
classification: county
fips: "29059"
state: "MO"
demographics:
  population: 17551
  population_under_18: 4143
  population_18_64: 9715
  population_65_plus: 3693
  median_household_income: 53464
  poverty_rate: 20.49
  homeownership_rate: 75.95
  unemployment_rate: 3.9
  median_home_value: 190300
  gini_index: 0.4699
  vacancy_rate: 11.1
  race_white: 16425
  race_black: 33
  race_asian: 3
  race_native: 16
  hispanic: 398
  bachelors_plus: 2931
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/142"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Dallas County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17551 |
| Under 18 | 4143 |
| 18–64 | 9715 |
| 65+ | 3693 |
| Median household income | 53464 |
| Poverty rate | 20.49 |
| Homeownership rate | 75.95 |
| Unemployment rate | 3.9 |
| Median home value | 190300 |
| Gini index | 0.4699 |
| Vacancy rate | 11.1 |
| White | 16425 |
| Black | 33 |
| Asian | 3 |
| Native | 16 |
| Hispanic/Latino | 398 |
| Bachelor's or higher | 2931 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 100% (congressional)
- [MO Senate District 28](/us/states/mo/districts/senate/28.md) — 100% (state senate)
- [MO House District 142](/us/states/mo/districts/house/142.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
