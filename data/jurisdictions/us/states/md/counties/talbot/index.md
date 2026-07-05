---
type: Jurisdiction
title: "Talbot County, MD"
classification: county
fips: "24041"
state: "MD"
demographics:
  population: 37917
  population_under_18: 7045
  population_18_64: 19662
  population_65_plus: 11210
  median_household_income: 84811
  poverty_rate: 9.33
  homeownership_rate: 75.07
  unemployment_rate: 4.33
  median_home_value: 409700
  gini_index: 0.5061
  vacancy_rate: 16.67
  race_white: 28647
  race_black: 4628
  race_asian: 528
  race_native: 187
  hispanic: 3650
  bachelors_plus: 17138
districts:
  - to: "us/states/md/districts/01"
    rel: in-district
    area_weight: 0.6708
  - to: "us/states/md/districts/senate/37"
    rel: in-district
    area_weight: 0.6449
  - to: "us/states/md/districts/house/37b"
    rel: in-district
    area_weight: 0.6449
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# Talbot County, MD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37917 |
| Under 18 | 7045 |
| 18–64 | 19662 |
| 65+ | 11210 |
| Median household income | 84811 |
| Poverty rate | 9.33 |
| Homeownership rate | 75.07 |
| Unemployment rate | 4.33 |
| Median home value | 409700 |
| Gini index | 0.5061 |
| Vacancy rate | 16.67 |
| White | 28647 |
| Black | 4628 |
| Asian | 528 |
| Native | 187 |
| Hispanic/Latino | 3650 |
| Bachelor's or higher | 17138 |

## Districts

- [MD-01](/us/states/md/districts/01.md) — 67% (congressional)
- [MD Senate District 37](/us/states/md/districts/senate/37.md) — 64% (state senate)
- [MD House District 37B](/us/states/md/districts/house/37b.md) — 64% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
