---
type: Jurisdiction
title: "Manassas Park city, VA"
classification: county
fips: "51685"
state: "VA"
demographics:
  population: 16798
  population_under_18: 4128
  population_18_64: 6622
  population_65_plus: 6048
  median_household_income: 103250
  poverty_rate: 5.12
  homeownership_rate: 66.47
  unemployment_rate: 5.54
  median_home_value: 395900
  gini_index: 0.3569
  vacancy_rate: 6.75
  race_white: 5543
  race_black: 2297
  race_asian: 1747
  race_native: 845
  hispanic: 7867
  bachelors_plus: 4359
districts:
  - to: "us/states/va/districts/10"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/30"
    rel: in-district
    area_weight: 0.9911
  - to: "us/states/va/districts/senate/29"
    rel: in-district
    area_weight: 0.0089
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Manassas Park city, VA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16798 |
| Under 18 | 4128 |
| 18–64 | 6622 |
| 65+ | 6048 |
| Median household income | 103250 |
| Poverty rate | 5.12 |
| Homeownership rate | 66.47 |
| Unemployment rate | 5.54 |
| Median home value | 395900 |
| Gini index | 0.3569 |
| Vacancy rate | 6.75 |
| White | 5543 |
| Black | 2297 |
| Asian | 1747 |
| Native | 845 |
| Hispanic/Latino | 7867 |
| Bachelor's or higher | 4359 |

## Districts

- [VA-10](/us/states/va/districts/10.md) — 100% (congressional)
- [VA Senate District 30](/us/states/va/districts/senate/30.md) — 99% (state senate)
- [VA Senate District 29](/us/states/va/districts/senate/29.md) — 1% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
